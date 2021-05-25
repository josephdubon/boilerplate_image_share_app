from django import forms
from django.contrib.auth.models import User
from .models import Profile


# Login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# User registration form
class UserRegistrationForm(forms.ModelForm):
    # two additional fields—password and password2
    # — for users to set their password and confirm it.
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        # Include only the username, first_name, and email fields of the model.
        fields = (
            'username',
            'first_name',
            'email',
        )

    def clean_password2(self):
        cd = self.cleaned_data
        #  Use the field-specific clean_password2() validation.
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']


# Edit user form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


# Edit user profile form
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'date_of_birth',
            'photo',
        )
