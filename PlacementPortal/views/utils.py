import datetime
from openpyxl import load_workbook

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from PlacementPortal.forms import UploadFileForm
from PlacementPortal.models import *


class Home(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "base.html"


def dept_push():
    fd = open("data/dept.csv", "r")

    for line in fd:
        fields = line[:-1].split(",")
        dept = Department(name=fields[1], acronym=fields[0])
        dept.save()


def get_data(file_name):
    wb = load_workbook(filename=file_name, read_only=True)
    ws = wb.active
    res = []
    for line in ws:
        row = []
        for cell in line:
            row.append(cell.value)
        res.append(row)
    wb.close()
    return res


def student_push(file_path):
    # dept_push()
    data = get_data(file_path)
    count = 1
    for row in data[1:]:
        print(count)
        count += 1
        try:
            student = Student.objects.get(hall_ticket_number=row[0])
        except Exception:
            # 1. Get the contact id
            contact = Contact(email=row[7], phone_number=str(row[6]), address=row[11],
                              guardian_parent_name=row[8], guardian_parent_contact=row[9],
                              guardian_parent_profession=row[10])
            contact.save()

            # 2. Get the department id
            department = Department.objects.get(acronym=row[1])

            # 3. Get the student id
            gender = 0
            if row[14] == "MALE":
                gender = 1
            student = Student(first_name=row[2], last_name=row[3], full_name=row[4], hall_ticket_number=row[0],
                              gender=gender, caste=row[15], career_goal=row[16], tenth_marks=row[12],
                              inter_marks=row[13], contact=contact, department=department, date_of_birth=row[5])
            student.save()


def marks_push(file_path):
    data = get_data(file_path)
    count = 1
    for row in data[1:]:
        if count % 100 == 0:
            print(count)
        count += 1

        try:
            student = Student.objects.get(hall_ticket_number__contains=row[0])
            try:
                marks = Marks.objects.get(subject_code__contains=row[1], student=student)
                marks.subject_name = row[2]
                marks.internal_marks = row[3]
                marks.external_marks = row[4]
                marks.total_marks = row[3] + row[4]
                marks.result = row[5]
                marks.save()
            except Exception:
                marks = Marks(
                    subject_code=row[1],
                    internal_marks=row[3],
                    subject_name=row[2],
                    external_marks=row[4],
                    total_marks=row[3] + row[4],
                    result=row[5],
                    student=student
                )
                marks.save()

        except Exception:
            pass


def refresh_btech_acads():
    students = Student.objects.all()

    count = 0

    for student in students:
        count += 1
        if count % 50 == 0:
            print(count)
        try:
            marks_list = Marks.objects.filter(student=student)

            backlogs = 0
            total = 0
            no_subjects = len(marks_list)
            for marks in marks_list:
                if marks.result == 'Fail':
                    backlogs += 1
                total += marks.total_marks

            btech_percentage = (total / (no_subjects * 100)) * 100

            student.btech_marks = btech_percentage
            student.backlogs = backlogs

            student.save()
        except marks_list.DoesNotExist:
            pass


def handle_uploaded_file(f, file_type):
    file_path = 'uploads/' + file_type + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.xlsx'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    if file_type == 'student':
        student_push(file_path)
    elif file_type == 'marks':
        marks_push(file_path)
    else:
        pass


def studentUpload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], 'student')
            return redirect('PlacementPortal:department_list')
    else:
        form = UploadFileForm()
    return render(request, 'PlacementPortal/upload.html', {'form': form, 'title': "Students Upload"})


def marksUpload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], 'marks')
            refresh_btech_acads()
            return redirect('PlacementPortal:department_list')
    else:
        form = UploadFileForm()
    return render(request, 'PlacementPortal/upload.html', {'form': form, 'title': "Marks Upload"})
