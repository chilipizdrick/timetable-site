from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from .models import UserProfile
from .forms import SignUpForm, LogInForm, ManageProfileForm


def index(request):
    if request.user.is_authenticated:
        return redirect('timetable')
    return render(request, 'index/index.html')


def timetable(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'GET':
        context = {'user': request.user}
        return render(request, 'timetable/index.html', context)

    if request.method == 'POST':
        # TODO: Implement timetable logic
        ...


def log_in(request):
    if request.user.is_authenticated:
        return redirect('timetable')

    if request.method == 'GET':
        context = {'form': LogInForm()}
        return render(request, 'account/login.html', context)

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'account/login.html', context)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid email or password.')
            context = {'form': form}
            return render(request, 'account/login.html', context)
        login(request, form.get_user())
        messages.success(
            request, f'You have logged in successfully as {user.username}.'
        )
        return redirect('timetable')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')

    if request.user.is_anonymous:
        return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('timetable')

    if request.method == 'GET':
        context = {'form': SignUpForm()}
        return render(request, 'account/signup.html', context)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'account/signup.html', context)

        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()

        UserProfile.objects.create(user=user)

        messages.success(request, 'You have singed up successfully.')
        login(request, user)
        return redirect('timetable')


def profile(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user,
            'user_profile': UserProfile.objects.filter(user=request.user),
        }
        return render(request, 'account/profile.html', context)

    if request.user.is_anonymous:
        return redirect('login')


def manage_profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            context = {'form': ManageProfileForm()}
            return render(request, 'account/manage_profile.html', context)

        if request.user.is_anonymous:
            redirect('login')

    if request.method == 'POST':
        # TODO: Implement account management logic
        ...
