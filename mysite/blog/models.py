from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 관리자 추가
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model): # Inheritance

    # List : choices
    # Key : labels
    # Value : values
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) # -> VARCHAR : 일반적으로 사용. 띄어쓰기 가능함.
    slug = models.SlugField(max_length=250) # -> VARCHAR : 소문자 + 하이픈(-)을 사용하는 게 컨벤션. URL 등에 적격
    # 다대일 관계 정의
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,    # 삭제 되면 같이 삭제 되게
                               related_name='blog_posts')   # User 에서 Post 로의 역방향 관계 명칭 지정.
    body = models.TextField() # TEXT
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # 객체를 생성할 때 날짜가 자동으로 저장된다.
    updated = models.DateTimeField(auto_now=True) # 객체를 저장할 때 날짜가 자동으로 저장된다.
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    # 기본 관리자
    objects = models.Manager()

    # 커스텀 관리자
    published = PublishedManager()

    class Meta: # 모델 내부에 Meta 클래스를 추가하여, 모델에 대한 메타데이터를 정의함.
        ordering = ['-publish'] # 출시일 역순으로 정렬
        indexes = [
            models.Index(fields=['-publish']), # 인덱스를 출시일 역순으로
        ]

    def __str__(self):
        return self.title