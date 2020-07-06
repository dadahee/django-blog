from django.db import models
from config import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()
    img = models.ImageField(upload_to='BlogApp/', blank=True, null=True) #media/BlogApp/파일이름 으로 저장
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likers')
    # pillow 패키지를 설치하여(pip install pillow) 이미지 파일 관리.

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.text)>100: return self.text[:100] + "..."
        return self.text


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments') #cascade option : 글이 삭제될 경우 덧글도 삭제 되도록 설정
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments') #set_null option
    text = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    ##### auto_now vs auto_now_add
    # auto_now : 최종 수정 일자
    # auto_now_add : 생성 일자

    def __str__(self):
        return f"{ self.author }님이 { self.blog } 글에 단 댓글"
    