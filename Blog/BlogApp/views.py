from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from .form import BlogForm


def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", { 'blogs': blogs })


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', { 'blog': blog })


def new(request):
    #1, 데이터가 입력된 후 제출 버튼을 누르면 데이터 저장 -> post 방식
    #2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 -> get 방식
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'new.html', { 'form': form })
    else:
        form = BlogForm(request.POST, request.FILES) #입력된 값으로 데이터를 저장할 것이므로 + file을 전달받기 위해 request.FILES도 추가
        # 입력 데이터 유효성 검사 해주기
        if form.is_valid():
            content = form.save(commit=False) #데이터 임시 저장(이후 살 붙이고 제대로 저장)
            content.date = timezone.now()
            content.save()
            return redirect('home')


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'GET':
        form = BlogForm(instance=edit_blog)
    else:
        form = BlogForm(request.POST, request.FILES, instance=edit_blog)
        # 입력 데이터 유효성 검사 해주기
        if form.is_valid():
            content = form.save(commit=False) #데이터 임시 저장(이후 살 붙이고 제대로 저장)
            content.date = timezone.now()
            content.save()
            return redirect('detail', content.id)
    return render(request, 'edit.html', { 'form': form, 'id': edit_blog.id })


def delete(request, blog_id):
    to_be_deleted = get_object_or_404(Blog, pk=blog_id)
    to_be_deleted.delete()
    return redirect('home')