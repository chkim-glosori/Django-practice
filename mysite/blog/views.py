from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts,
                  'tag': tag})

class PostListView(ListView):
    """
    Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form,
                   'similar_posts': similar_posts})

def post_share(request, post_id):

    # 1. 일단 게시물을 조회하게 놔 둬.
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    # 2. 근데 만약 POST 라면 == 폼이 제출되었다면
    if request.method == "POST":

        # 2-1. form 이라는 변수에 해당 입력 값들을 할당.
        form = EmailPostForm(request.POST)

        # 2-2. form 이라는 변수에 할당된 값들이 유효한가?
        if form.is_valid():
            cd = (
                form.cleaned_data
            )  # 폼 데이터가 유효하지 않다면, 유효한 필드만 포함하게 만듦.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(subject, message, "your_account@gmail.com", [cd["to"]])
            sent = True

    # 3. POST 가 아니라면 == 제출하기 전이다.
    else:
        form = EmailPostForm()  # 템플릿에 비어 있는 폼을 표시하는 데 사용된다.

    # blog/templates/blog/post/share.html 하면 오류가 남. templates 디렉터리까지는 내가 설정해 줬나 봄.
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )


@require_POST  # 이 뷰에는 POST 요청만을 허용하게 함.
def post_comment(request, post_id):  # 이 두 파라미터가 하는 일 :
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None

    # 댓글이 달림
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(
            commit=False
        )  # 데이터베이스에 저장하지 않고 Comment 객체 만들기
        comment.post = post  # Post 가 할당이 되면
        comment.save()  # 그 다음에 save()
    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )