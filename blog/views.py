from django.shortcuts import render


# Create your views here.
def posts(request):
    return render(request, 'home/posts.html')


def post(request, title):
    return render(request, 'home/post.html')
