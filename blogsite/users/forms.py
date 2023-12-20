from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from .enums import UserRoles
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email',]:
            self.fields[fieldname].help_text = None
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']

class UserRoleForm(forms.Form):
    role_choices = [(role.name, role.name) for role in UserRoles]
    user_role = forms.TypedChoiceField(choices=role_choices, label='User Role', coerce=str)