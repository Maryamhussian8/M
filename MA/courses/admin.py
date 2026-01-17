from django.contrib import admin
from .models import College, Section, Stage, Subject, Chapter, User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'college_name']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'sec_name', 'college']
    list_filter = ['college']


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['id','stage_name', 'section']
    list_filter = ['section']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'college', 'section', 'stage']
    list_filter = ['college', 'section', 'stage']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter_name', 'subject', 'youtube_link']
    list_filter = ['subject']
    search_fields = ['chapter_name']





admin.site.unregister(User)
@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
