from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import  Articles
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Profile
from .forms import LoginForm, RegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, HttpResponse

from .forms import UserEditForm, ProfileEditForm
from  django.http import HttpResponseRedirect, HttpResponse
'''Вход'''


def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                try:
                    login(request, user)
                    return redirect('index')
                except:
                    context = {
                    'form': forms,
                    'error': 'Данный логин недействителен либо неверный пароль'
                    }
                    return render(request, 'signin.html', context)

    context = {
        'form': forms,

    }
    return render(request, 'signin.html', context)



'''Регистрация'''


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)

        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']

            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)

                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'Этот логин уже используется !'

                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)


'''Выход'''


def signout(request):
    logout(request)
    return redirect('index')


'''Редактирование профиля'''

from django.template import RequestContext

@login_required
def edit(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        profile = Profile.objects.filter(photo=request.user.profile.photo)


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        return render(request,
                  'profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   "profile": profile,

                   })

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        profile = Profile.objects.filter(photo=request.user.profile.photo)
        return render(request,
                      'profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       "profile":profile})
