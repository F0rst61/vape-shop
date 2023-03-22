from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
