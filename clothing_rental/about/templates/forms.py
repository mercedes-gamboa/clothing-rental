# from django import forms
#
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Your Name', max_length=100)
#     email = forms.EmailField(label='Your Email')
#     message = forms.CharField(label='Your Message', widget=forms.Textarea)
#
#     def send_email(self):
#         name = self.cleaned_data['name']
#         email = self.cleaned_data['email']
#         message = self.cleaned_data['message']
#
#         subject = f"Contact Form Submission from {name}"
#         content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
#
#         # Replace 'your_superuser_email' with the email address of the superuser
#         # Ensure that you have configured the email settings in Django settings.py file
#         # Refer to Django documentation for more information on email configuration
#
#         from_email = 'noreply@example.com'  # Update with your email address
#         to_email = ['your_superuser_email']
#
#         send_mail(subject, content, from_email, to_email, fail_silently=False)