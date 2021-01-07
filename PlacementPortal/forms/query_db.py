from django import forms
from PlacementPortal.models import *


class GetStudentDetails(forms.Form):
    try:
        GENDER = (
            ("0", "ALL"),
            ("Male", 'Male'),
            ("Female", 'Female')
        )
        departments = Department.objects.values('acronym')
        DEPT = (("0", "ALL"),)

        for index in departments:
            branch = (index['acronym'], index['acronym'])
            DEPT = DEPT.__add__((branch,))

        CASTE = (
            ("0", "ALL"),
            ("OC", "OC"),
            ("SC", "SC"),
            ("ST", "ST"),
            ("BC", "BC"),
        )

        gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER)

        caste = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CASTE)

        department = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DEPT)

        tenth = forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10th marks'})
        )

        inter = forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control lol', 'placeholder': 'Enter Inter Marks'})
        )
        btech = forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter B.Tech Marks'})
        )
        backlogs = forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Backlogs'})
        )
    except:
        pass



# class GetStudentDetails(forms.ModelForm):

# class Meta:
#     model = Student
#     # exclude = ['id']
#     fields = ['gender', 'tenth_marks', 'inter_marks', 'btech_marks', 'backlogs']
#     widgets = {
#
#         'gender': forms.CheckboxInput(attrs={'class': 'form-control'}),
#
#         'tenth_marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10th marks'}),
#
#         'inter_marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Inter marks'}),
#
#         'btech_marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter B.Tech marks'}),
#
#         'backlogs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Backlogs'}),
#
#     }
