from django import forms
from PlacementPortal.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['id']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Form'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Acronym'}),
        }
