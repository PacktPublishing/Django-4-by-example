from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')                                      # edited
    try:                                                                       # new
        posts = paginator.page(page_number)                                    # new
    except EmptyPage:                                                          # new
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)                            # new
    return render(request,
                  'blog/post/list.html',
                   {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
