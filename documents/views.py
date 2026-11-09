
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.decorators.http import require_POST

from .models import Document
from .utils import extract_text
from .llm import chat


def upload_document(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        file = request.FILES.get("file")

        if not title or not file:
            return redirect("upload")

        try:
            text = extract_text(file)

            with transaction.atomic():
                Document.objects.create(
                    title=title,
                    file=file,
                    extracted_text=text,
                )

            return redirect("upload")

        except Exception as e:
            return render(request, "documents/upload.html", {
                "documents": Document.objects.order_by("-uploaded_at"),
                "error": str(e),
            })

    return render(request, "documents/upload.html", {
        "documents": Document.objects.order_by("-uploaded_at"),
    })


@require_POST
def summarize_document(request, pk):
    document = get_object_or_404(Document, pk=pk)

    if not document.extracted_text.strip():
        return render(request, "documents/upload.html", {
            "documents": Document.objects.order_by("-uploaded_at"),
            "error": "추출된 텍스트가 없습니다.",
        })

    if len(document.extracted_text) > 20000:
        return render(request, "documents/upload.html", {
            "documents": Document.objects.order_by("-uploaded_at"),
            "error": "문서가 너무 깁니다. 최대 20,000자까지 지원합니다.",
        })

    try:
        document.summary = chat(
            f"다음 문서를 한국어로 요약해줘.\n\n{document.extracted_text}",
            "너는 전문적인 한국어 문서 요약 AI야. "
            "핵심 주제, 주요 내용, 결론을 정리해."
        )
        document.save(update_fields=["summary"])

        return redirect("upload")

    except Exception as e:
        return render(request, "documents/upload.html", {
            "documents": Document.objects.order_by("-uploaded_at"),
            "error": f"요약 실패: {e}",
        })
