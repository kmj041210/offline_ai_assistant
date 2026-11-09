from django.shortcuts import render

# 

from django.shortcuts import render, redirect
from .models import Document


def upload_document(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        file = request.FILES.get("file")

        if title and file:
            Document.objects.create(title=title, file=file)
            return redirect("upload")

    documents = Document.objects.order_by("-uploaded_at")
    return render(request, "documents/upload.html", {
        "documents": documents
    })
