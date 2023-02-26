from django.urls import path

from blog.views import posts,post

app_name = "blog"
urlpatterns= [
    path("", posts,  name="posts"),
    path("<str:title>/", post,  name="post"),
]