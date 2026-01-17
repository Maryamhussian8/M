from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CollegeViewSet, SectionViewSet, StageViewSet, SubjectViewSet, ChapterViewSet, RegisterWatchHistoryView, WatchHistoryListView, ChapterListFilteredView, get_sections_by_college, get_stages_by_section, get_subjects_by_stage


router = DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'stages', StageViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'chapters', ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('watch/register/', RegisterWatchHistoryView.as_view(), name='register-watch-history'),
    path('watch-history/list/', WatchHistoryListView.as_view(), name='watch-history-list'),
    path('api/chapters/filter/', ChapterListFilteredView.as_view(), name='chapter-filter'),
    path('api/sections/', get_sections_by_college, name='api_sections'),
    path('api/stages/', get_stages_by_section, name='api_stages'),
    path('api/subjects/', get_subjects_by_stage, name='api_subjects'),

]
