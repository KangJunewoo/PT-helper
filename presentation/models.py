from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class PDF(models.Model):
    # id는 기본 값으로 주어지니까 그걸 primary key로 사용해서 quecard가 그걸 참조
    title = models.CharField(max_length=20) # 제목
    author = models.Foreignkey(Profile, null=False) # 작성자
    text = models.TextField(null=False) # 간단한 소개 (이건 할지 말지 정하기.)
    pdffile = models.FileField(upload_to ="pdf", null=False) # pdf파일
    written_date = models.DateTimeField(default=timezone.now, null=False) # 처음 올린 날
    latest_date = models.DateTimeField(null=False) # 마지막으로 건드린 날
    category = models.IntegerField(default=0) # 추후 폴더 관리
    
    def __str__(self):
        return self.title

# 큐카드 하나하나를 의미하고, 하나의 PDF모델에는 여러 개의 Quecard 모델이 연결
class Quecard(models.Model):
    pdffile = models.Foreignkey(PDF, null=False) # PDF파일 id 값 들어감
    name = models.CharField(max_length=30, null=False) # 이미지 파일별 이름, 제목+sequence
    image = models.ImageField(upload_to="slides") # 큐카드 만들어질 때 View에서 사용자별 폴더를 만들어서 저장될 수 있게 구현
    sequence = models.IntegerField(null=False) # 제목 뒤에 인덱스로 할 수도 있는데 간단하게 sequence로 츨력, sequence 0값이 썸네일
    text = models.TextField(null=False)
    time_min = models.IntegerField(default=0) # 이건 웹에서는 안 쓰고 나중에 앱으로 넘겨줄 큐카드별 시간
    time_sec = models.IntegerField(default=0)

    def __str__(self):
        return self.sequence