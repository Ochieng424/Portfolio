from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    fullName = forms.CharField(label='Full Name')

    class Meta:
        model = Contact
        fields = [
            'fullName',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            'message': forms.Textarea(attrs={"rows": 4})
        }
