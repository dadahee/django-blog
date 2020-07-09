from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone

from .form import BlogForm


def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", { 'blogs': blogs })


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog)
    likers = blog.like.all()
    return render(request, 'detail.html', { 'blog': blog, 'comments': comments, 'likers': likers })


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
            content.writer = request.user
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
            #content.date = timezone.now()
            content.writer = request.user #사실상 필요 없으나 이후를 위해 추가해놓음
            content.save()
            return redirect('detail', content.id)
    return render(request, 'edit.html', { 'form': form, 'id': edit_blog.id })


def delete(request, blog_id):
    to_be_deleted = get_object_or_404(Blog, pk=blog_id)
    to_be_deleted.delete()
    return redirect('home')



def new_comment(request, blog_id):
    new_comment = Comment()
    new_comment.blog = get_object_or_404(Blog, pk=blog_id)
    new_comment.author = request.user
    new_comment.text = request.POST.get('text')
    new_comment.save()
    return redirect('detail', blog_id)

def edit_comment(request, comment_id):
    edit_comment = get_object_or_404(Comment, pk=comment_id)
    blog_id = edit_comment.blog.id
    if request.method == "GET":
        blog = get_object_or_404(Blog, pk=blog_id)
        comments = Comment.objects.filter(blog=blog)
        likers = blog.like.all()
        return render(request, 'comment_edit.html', { 'blog': blog, 'comments': comments, 'likers': likers, 'edit_comment': edit_comment })
    else:
        edit_comment.text = request.POST.get('text')
        edit_comment.save()
        return redirect('detail', blog_id)

def del_comment(request, comment_id):
    del_comment = get_object_or_404(Comment, pk=comment_id)
    blog_id = del_comment.blog.id
    del_comment.delete()
    return redirect('detail', blog_id)

def like(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # get 방식일 때에는 좋아요 추가, post 방식일 때에는 좋아요 취소
    if request.method == "GET":
        blog.like.add(request.user)
    else:
        blog.like.remove(request.user)
    blog.save()
    return redirect('detail', blog_id)