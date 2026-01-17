from django.shortcuts import render, get_object_or_404, redirect
from .models import College, Section, Stage, Subject, Chapter, WatchHistory
from .forms import CourseSelectionForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import requests
from django.shortcuts import render
from django.conf import settings


def chapter_list_view(request):
    college_id = request.GET.get('college')
    section_id = request.GET.get('section')
    stage_id = request.GET.get('stage')
    subject_id = request.GET.get('subject')

    chapters = Chapter.objects.all()
    college = section = stage = subject = None

    if college_id:
        college = College.objects.filter(id=college_id).first()
        chapters = chapters.filter(college_id=college_id)
    if section_id:
        section = Section.objects.filter(id=section_id).first()
        chapters = chapters.filter(section_id=section_id)
    if stage_id:
        stage = Stage.objects.filter(id=stage_id).first()
        chapters = chapters.filter(stage_id=stage_id)
    if subject_id:
        subject = Subject.objects.filter(id=subject_id).first()
        chapters = chapters.filter(subject_id=subject_id)

    if request.user.is_authenticated:
        watch_history = WatchHistory.objects.filter(
            user=request.user
        ).order_by('-watched_at')[:5]
    else:
        watch_history = None

    context = {
        'chapters': chapters,
        'college': college,
        'section': section,
        'stage': stage,
        'subject': subject,
        'watch_history': watch_history,   
    }

    return render(request, 'chapters.html', context)


def select_course_view(request):
    form = CourseSelectionForm(request.GET or None)
    chapters = None

    if form.is_valid():
        college = form.cleaned_data.get('college')
        section = form.cleaned_data.get('section')
        stage = form.cleaned_data.get('stage')
        subject = form.cleaned_data.get('subject')
        chapters = Chapter.objects.filter(
            college=college, section=section, stage=stage, subject=subject
        ).order_by('id')

    return render(request, 'select_course.html', {'form': form, 'chapters': chapters})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('select-course')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('select-course')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def watch_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)

    if request.user.is_authenticated:
        WatchHistory.objects.create(
            user=request.user,
            chapter=chapter
        )

    return redirect(chapter.youtube_link)

def full_watch_history(request):
    if not request.user.is_authenticated:
        return redirect('login')

    history = WatchHistory.objects.filter(
        user=request.user
    ).order_by('-watched_at')

    return render(request, 'full_watch_history.html', {'history': history})
