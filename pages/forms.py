from django import forms

from .models import Contact



class ContactForm(forms.ModelForm):

    fullName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Full Name', 'type': 'text'}), label='')
    phone = forms.CharField(widget=forms.TextInput({'placeholder': 'Phone Number', 'type': 'tel'}), label='')
    email = forms.CharField(widget=forms.TextInput({'placeholder': 'Email Address', 'type': 'email'}), label='')
    message = forms.CharField(widget=forms.Textarea({'placeholder': 'Your Message'}), label='')

    class Meta:
        model = Contact
        fields = ('fullName', 'phone', 'email', 'message')





