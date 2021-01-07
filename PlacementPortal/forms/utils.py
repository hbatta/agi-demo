from django import forms

from PlacementPortal.models import Student, Contact, Marks, Department


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'contact']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['id']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['id']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        exclude = ['id', 'student']


class UploadFileForm(forms.Form):
    # title = forms.CharField(
    #     max_length=50,
    #     required=True,
    # )

    file = forms.FileField(
        allow_empty_file=False,
    )
