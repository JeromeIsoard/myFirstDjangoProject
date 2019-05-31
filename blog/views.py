from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.shortcuts import redirect
from pprint import pprint

from blog.templates.blog.forms import PostForm
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

User = get_user_model()


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    users = User.objects.all()
    print(users)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
