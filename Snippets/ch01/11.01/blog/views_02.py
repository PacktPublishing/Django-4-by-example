from django.shortcuts import render
from django.http import Http404                                                # new
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})
# new block
def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
#