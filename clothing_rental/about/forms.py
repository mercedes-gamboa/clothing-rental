from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)