from django.urls import path
from .views import (
HomeView,
ExamView,
CourseView,
CourseCreateView,
course_single,
AssignmentCreateView,
AssignmentView,
AssignmentDeleteView,
ExamCreateView,
ExamListView,
AssignmentSubmissionView,
ExamDeleteView,
ExamSubmissionView,
ExamSubmissionListView,
AssignmentSubmissionListView,
AssignmentSubmissionDelete,
ExamSubmissionDelete

)
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('exam/', ExamView.as_view(), name='exam'),
                  path('course/', CourseView.as_view(), name='course'),
                  path('course-create/', CourseCreateView.as_view(), name='course-create'),
                  path('assignment-create/', AssignmentCreateView.as_view(), name='assignment-create'),
                  path('assignment/', AssignmentView.as_view(), name='assignment-list'),
                  path('<pk>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),
                  path('<int:id>/course-view/', course_single, name='course-view'),
                  path('exam-create/', ExamCreateView.as_view(), name='exam-create'),
                  path('exam-list/', ExamListView.as_view(), name='exam-list'),
                  path('<pk>/delete/', ExamDeleteView.as_view(), name='delete-exam'),
                  path('assignment-submission/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
                  path('exam-submission/', ExamSubmissionView.as_view(), name='exam-submission'),
                  path('exam-submission-list/', ExamSubmissionListView.as_view(), name='exam-submission-list'),
                  path('assignment-submission-list/', AssignmentSubmissionListView.as_view(), name='assignment-submission-list'),
                  path('<pk>/delete/', AssignmentSubmissionDelete.as_view(), name='assignment-submission-delete'),
                  path('<pk>/delete/', ExamSubmissionDelete.as_view(), name='exam-submission-delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
