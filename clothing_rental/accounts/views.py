from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

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
             return redirect("/")

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