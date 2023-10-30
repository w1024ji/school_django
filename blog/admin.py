from django.contrib import admin

# Register your models here.

# Post 모델을 등록함
from .models import Post

admin.site.register(Post)
