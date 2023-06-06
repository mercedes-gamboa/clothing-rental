from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from .forms import ContactForm


# Create your views here.
def about_page(request):
    return render(request, 'about/about.html')

class ContactUs(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact_us.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['your-email@example.com'],  # Replace with your email address
                fail_silently=False,
            )

            return render(request, 'contact_success.html')

        return render(request, 'contact_us.html', {'form': form})