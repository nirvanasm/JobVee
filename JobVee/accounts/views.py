from django.http import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm, EditProfileForm, EditUserForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

startTemplate = 'webapp/header.html'
loginTemplate = 'webapp/loginHeader.html'

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../home')
    
    return HttpResponseRedirect('../home')
    #return render('webapp/account/login.html', context_instance=RequestContext(request))

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            user.profile.city = form.cleaned_data.get('city')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password  = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/account/userProfile.html')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'webapp/account/register.html',{'form': form})

def view_profile(request):
    args = { 'user': request.user }
    return render(request, 'webapp/account/profile.html',{'base_template': loginTemplate,  'user': request.user   } )


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance = request.user)
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/account/userProfile.html')
        return HttpResponseRedirect('/')
    else:
        user_form = EditUserForm(request.POST, instance = request.user)
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        return render(request, 'webapp/account/editProfile.html', {
            'user_edit_form': user_form,
            'profile_edit_form': profile_form, 
            'base_template': loginTemplate
        })
