from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, year, month, day, post):                              # edited
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,                     # edited
                             slug=post,                                        # new
                             publish__year=year,                               # new
                             publish__month=month,                             # new
                             publish__day=day)                                 # new
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
