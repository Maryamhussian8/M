from django.urls import path
from .views import chapter_list_view, select_course_view, login_view,register_view, watch_chapter, full_watch_history

urlpatterns = [
    path('', select_course_view, name='select-course'),        
    path('chapters/', chapter_list_view, name='chapter-list-page'),  
    path('login/', login_view,name='login'),
    path('register/', register_view, name='register'),
    path('watch/<int:chapter_id>/', watch_chapter, name='watch-chapter'),
    path('watch-history/', full_watch_history, name='full-watch-history'),


    
]
