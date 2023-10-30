from django.db import models
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30) # CharField는 문자를 담는 필드
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() # 문자열의 길이 제한이 없는 TextField를 사용

    # 미디어 파일 관리하기 위해 추가함 (아랫줄)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # DateTimeField는 월, 일, 시, 분, 초까지 기록할 수 있게 해주는 필드를 만들 때 사용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author field will be later written

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]