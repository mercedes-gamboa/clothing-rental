from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="A valid email address, please.", required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()

        return user

class ProfileForm(forms.ModelForm):
    #  is this argument correct?
    class Meta:
        model = Profile
        fields = ('address', 'phone', 'birth_date')


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

