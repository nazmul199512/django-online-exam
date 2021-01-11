from django.contrib import admin
from .models import Course, Assignment, Exam, AssignmentSubmission, ExamSubmission

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(AssignmentSubmission)
admin.site.register(ExamSubmission)
