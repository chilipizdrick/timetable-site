from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'A user with this email already exists.')
        return email


class LogInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            self.add_error(
                'username', 'A user with this username does not exist.'
            )
            return username

        user = User.objects.get(username=username)
        if not user.check_password(password):
            self.add_error('password', 'Entered password is incorrect.')
            return password

        return self.cleaned_data

    def get_user(self):
        username = self.cleaned_data['username']
        user = User.objects.get(username=username)
        return user


class ManageProfileForm(forms.Form):
    # TODO: Implement the form
    ...
