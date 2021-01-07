from django import forms
from PlacementPortal.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = []