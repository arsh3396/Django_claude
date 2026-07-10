from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=2,
        error_messages={
            'min_length': 'Name must be at least 2 characters',
            'required': 'Please enter your name'
        }
    )
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        error_messages={
            'min_length': "Message must be at least 10 characters"
        }
    )