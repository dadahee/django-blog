from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.TextField()
    img = models.ImageField(upload_to='BlogApp/', blank=True, null=True) #media/BlogApp/파일이름 으로 저장
    # pillow 패키지를 설치하여(pip install pillow) 이미지 파일 관리.

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.text)>100: return self.text[:100] + "..."
        return self.text