from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.contrib import messages
from django.core.urlresolvers import reverse



# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post_detail':post_detail})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '글이 생성됐습니다.')
            return redirect(reverse('blog:detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '글이 수정됐습니다.')
            return redirect(reverse('blog:detail', args=[post.pk]))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save()
            messages.success(request, '댓글이 생성됐습니다.')
            return redirect(reverse('blog:detail', args=[post_pk]))
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})
