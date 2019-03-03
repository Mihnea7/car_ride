from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

# Create your views here.

def home(request):
    context_dict ={}
    response = render(request, 'carride/home.html', context=context_dict)
    return response

def about(request):
    context_dict={}
    response = render(request, 'carride/about.html', context=context_dict)
    return response

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                'rango/register.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered})      

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Carride account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'carride/login.html', {})

@login_required
def restricted(request):
    return render(request, 'carride/restricted.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


