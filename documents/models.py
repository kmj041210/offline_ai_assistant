from django.db import models
from django.core.validators import FileExtensionValidator


class Document(models.Model): # 문서 데이터 모델
    title = models.CharField(max_length=200) # CharField: 문자열 저장, max_length: 최대 길이 제한
    file = models.FileField(                 # FileField: PDF 파일 저장, upload_to: 업로드 경로 지정
        upload_to="documents/",              # upload_to: 파일저장 폴더 
        validators=[FileExtensionValidator(["pdf"])]
    )
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField: 생성날짜 저장

    def __str__(self):          # __str__ : 관리자 페이지에서 보일 이름
        return self.title
