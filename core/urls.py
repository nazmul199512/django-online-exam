from django.urls import path
from .views import HomeView, ExamView, CourseView


app_name = "core"

urlpatterns = [
    path('', HomeView.as_view()),
    path('exam/', ExamView.as_view(), name='exam'),
    path('course/', CourseView.as_view(), name='course'),
]
