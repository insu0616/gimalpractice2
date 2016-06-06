from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post_detail':post_detail})
