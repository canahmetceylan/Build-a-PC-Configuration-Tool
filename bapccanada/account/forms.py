from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField

from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.forms import ModelForm

from account.models import UserProfile


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(
        label="Birth date",
        help_text="YYYY-MM-DD",
        required=True
    )

    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date']

    # def save(self, commit=True):
    #     if not commit:
    #         raise NotImplementedError("Can't create User and UserProfile without database save")
    #     user = super(SignUpForm, self).save(commit=True)
    #     user_profile = UserProfile(user=user, birth_date=self.cleaned_data['birth_date'])
    #     user_profile.save()
    #     return user, user_profile

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=True)
        user_profile = UserProfile(user=user, birth_date=self.cleaned_data['birth_date'])
        if commit:
            user_profile.save()
        return user
