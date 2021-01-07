from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from PlacementPortal.models import Student
from django.http import HttpResponse
from wsgiref.util  import FileWrapper
from django.core.files import File

import os
from PlacementPortal.forms import StudentForm, ContactForm


class StudentList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Student
    template_name = "PlacementPortal/student_list.html"

    def get_queryset(self):
        return Student.objects.values(
            'pk',
            "full_name",
            "hall_ticket_number",
            "department__acronym",
            "date_of_birth",
            "gender",
            "caste",
            "tenth_marks",
            "inter_marks"
        ).order_by("pk")


def send_file(request):
    filepath = 'C:\collegeProject\ExamDeptProject\data\contact.csv'
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=C:\collegeProject\ExamDeptProject\data\contact.csv'
    return response
