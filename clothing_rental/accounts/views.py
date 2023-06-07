from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from accounts.forms import UserRegistrationForm, UserLoginForm, ProfileForm

# Create your views here.

User = get_user_model()

def register(request):
     if request.user.is_authenticated:
         return redirect('/')

     if request.method == "POST":
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             data = form.cleaned_data
             user = User.objects.create_user(email=data["email"], password=data["password1"], first_name=data["first_name"], last_name=data["last_name"])
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
    if request.method == "GET":
        form = ProfileForm()

        return render(
            request,
            "profile.html",
            {"form": form}
        )
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

class Home(TemplateView):
    template_name = "home.html"

def login_view(request):
    if request.method == "GET":
        form = UserLoginForm()

        return render(
            request,
            "login.html",
            {"form": form}
        )

    elif request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

        return render(
            request,
            "login.html",
            {"form": form}
        )


def logout_view(request):
    logout(request)
    return redirect('home')

