from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from accounts.forms import UserRegistrationForm

# Create your views here.

def register(request):
     if request.user.is_authenticated:
         return redirect('/')

     if request.method == "POST":
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect("/home")

         else:
             for error in list(form.errors.values()):
                 print(request, error)

     else:
         form = UserRegistrationForm()

     return render(
         request=request,
         template_name="register.html",
         context={"form":form}
     )

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

# def user_login(request):
#     username = request.POST["email"]
#     password = request.POST["password"]
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/home")
#
#     else:
#         print("Please try again.")

class Home(TemplateView):
    template_name = "home.html"
