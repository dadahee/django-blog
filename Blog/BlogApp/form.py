from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        # 어떤 모델을 기반으로 입력 받을 건지
        model = Blog
        # 원하는 값, 다른 곳에서 처리하려면 view에서 처리...
        fields = ['title', 'text', 'img'] 
