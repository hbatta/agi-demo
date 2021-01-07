from django import forms
from PlacementPortal.models import Student, Contact




class StudentForm(forms.ModelForm):
    GENDER_CHOICE = (
        (0,"Select Gender"),
        (1, "Male"),
        (2, 'Female')
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICE)

    class Meta:
        model = Student
        exclude = ['contact','gender']

        def save(self,commit=True):
            return super(StudentForm,self).save(commit=commit)


