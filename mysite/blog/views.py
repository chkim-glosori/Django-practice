from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

def post_list(request):
    posts = Post.published.all() # 커스텀 관리자
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    
    # get_object_or_404 메서드가 아닌 get() 메서드를 사용한 할 경우의 예외 처리
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})