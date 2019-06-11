from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


class AddStudent(CreateView):
    model = Student
    template_name = 'add.html'
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('list')


class StudentList(ListView):
    model = Student
    template_name = 'list.html'
    context_object_name = 'students'



