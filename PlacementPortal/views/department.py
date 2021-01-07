from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from PlacementPortal.models import Department, Student
from PlacementPortal.forms import DepartmentForm, StudentForm, ContactForm


class DepartmentList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Department
    template_name = "PlacementPortal/department_list.html"


class DepartmentDelete(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    slug_url_kwarg = 'dept_id'
    model = Department
    template_name = "PlacementPortal/department_delete.html"
    success_url = reverse_lazy("PlacementPortal:home")


class DepartmentCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Department
    template_name = "PlacementPortal/department_form.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("PlacementPortal:department_list")


class DepartmentUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Department
    template_name = "PlacementPortal/department_form.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("PlacementPortal:department_list")


class DepartmentStudentList(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Student
    template_name = "PlacementPortal/student_list.html"

    def get_object(self, queryset=None):
        object = Student.objects.values(
            "id",
            "full_name",
            "hall_ticket_number",
            "department__acronym",
            "date_of_birth",
            "gender",
            "caste",
            "tenth_marks",
            "inter_marks",
            "department_id",
            "btech_marks",
            "backlogs"
        ).filter(department_id=self.kwargs.get('dept_id'))
        return object

    def get_context_data(self, **kwargs):
        context = super(DepartmentStudentList, self).get_context_data(**kwargs)
        student_list = context.get('object')
        context.update(
            {
                'student_list': student_list
            }
        )
        return context


class DepartmentStudentEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Student
    template_name = "PlacementPortal/student_form.html"
    form_class = StudentForm
    success_url = reverse_lazy("PlacementPortal:department_list")

    def get_context_data(self, **kwargs):
        context = super(DepartmentStudentEdit, self).get_context_data(**kwargs)
        student_form = context.get("form")
        contact_form = ContactForm(instance=self.get_object().contact)
        context.update(
            {
                'student_form': student_form,
                'contact_form': contact_form,
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))

        getGenderUpdate = request.POST['gender']

        if int(getGenderUpdate) == 1:
            student.gender = True
        else:
            student.gender = False

        student_form = StudentForm(request.POST, instance=student)
        contact_form = ContactForm(request.POST, instance=student.contact)

        contact_form.save()
        student_form.save()

        return redirect("PlacementPortal:department_list")