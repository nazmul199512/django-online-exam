from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class ExamView(TemplateView):
    template_name = 'core/exams.html'


class CourseView(TemplateView):
    template_name = 'core/courses.html'
