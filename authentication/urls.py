from django.urls import path
from .views import *


app_name = "authentication"

urlpatterns = [
    path('student/register', RegisterStudentView.as_view(), name='student-register'),
    path('student/profile/update/', EditStudentProfileView.as_view(), name='student-profile-update'),
    path('instructor/register', RegisterInstructorView.as_view(), name='instructor-register'),
    path('instructor/profile/update/', EditInstructorProfileView.as_view(), name='instructor-profile-update'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
