from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"), #위는 늘 같은 url, 얘는 다를 수 있음.
    # id값을 어떻게 넘기지? 에 대한 답.
    # path converter : html상에서 요청을 보내면 보내준 값을 url을 이용해 넘길 수 있음.
    path('new/', views.new, name="new"),
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
    path('new_comment/<int:blog_id>', views.new_comment, name="new_comment"),
    path('edit_comment/<int:comment_id>', views.edit_comment, name="edit_comment"),
    path('del_comment/<int:comment_id>', views.del_comment, name="del_comment"),
    path('like/<int:blog_id>', views.like, name="like")
] 