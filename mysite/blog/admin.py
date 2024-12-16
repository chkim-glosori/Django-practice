from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)  # Post 모델을 Django Admin에 등록
class PostAdmin(admin.ModelAdmin):  # Post 모델을 위한 Admin 커스터마이징 클래스

    list_display = ['title', 'slug', 'author', 'publish', 'status']  # Admin 리스트 페이지에 표시할 필드
    list_filter = ['status', 'created', 'publish', 'author']  # 필터 사이드바에 표시할 필드
    search_fields = ['title', 'body']  # Admin 검색 박스에서 검색할 필드
    prepopulated_fields = {'slug': ('title', )}  # 제목을 기반으로 슬러그 자동 생성
    raw_id_fields = ['author']  # 작성자 필드를 Raw ID 필드로 표시 (드롭다운 대신)
    date_hierarchy = 'publish'  # 날짜 계층 구조를 사용하여 게시 날짜로 필터링
    ordering = ['status', 'publish']  # 기본 정렬 기준 (상태, 발행일)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active'] # Admin 리스트 페이지에 표시할 필드
    list_filter = ['active', 'created', 'updated'] # 필터 사이드바에 표시할 필드
    search_fields = ['name', 'email', 'body'] # Admin 검색 박스에서 검색할 필드