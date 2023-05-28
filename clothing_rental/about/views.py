from django.shortcuts import render


# from about.forms import ContactForm
# from django.core.mail import send_mail

# Create your views here.
def about_page(request):
    return render(request, 'about/about.html')

# def about_page(request):
#     form = ContactForm()
#
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.send_email()
#             form = ContactForm()  # Reset the form after submission
#         # Handle form submission (e.g., send email)
#         # Replace this with your own logic
#
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#
#         # Replace this with your own logic to handle form submission
#         # For example, you can send an email using Django's EmailMessage class
#         # Refer to Django documentation for more information
#
#         # Reset the form after submission
#         form = ContactForm()
#
#
#     return render(request, 'about/about.html', {'form': form})


# def about_page(request):
#     form = ContactForm()
#
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.send_email()
#             form = ContactForm()  # Reset the form after submission
#
#     return render(request, 'about/about.html', {'form': form})
