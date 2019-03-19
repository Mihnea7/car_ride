from django.shortcuts import render, redirect
from django.http import HttpResponse
from carride.forms import UserForm, UserProfileForm, ReviewForm, VehicleForm, CompareForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.core.urlresolvers import reverse
from carride.models import Vehicle, Review, UserProfile
from django.core.paginator import Paginator
from django.db.models import Avg, Func
from django.contrib.auth.models import User
# Create your views here.


class Round(Func):
    function='ROUND'
    arity=2

def home(request):
    context_dict ={}
    context_dict['top_cars'] = Vehicle.objects.order_by('-rating')[:3]
    
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
                'carride/register.html',
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
def MyAccount(request):
    context_dict={}
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
        context_dict['picture'] = profile.picture
    except:
        context_dict['default'] = 'default'
    response = render(request, 'carride/myaccount.html',context_dict)
    return response

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# each view returns HttpResponse object - takes string
# as a parameter representing the content of the page 
# to be sent to the client

def show_car_details(request, model_slug):
    context_dict = {}

    print("Hello")

    print(request.user)
    
    try:
        car = Vehicle.objects.get(slug=model_slug)
        context_dict['chosen_car'] = car
    except Vehicle.DoesNotExist:
        context_dict['chosen_car'] = None

    form = ReviewForm()

    if request.method == 'POST':
        # starting point???
        form = ReviewForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = car

            #current_user = request.user
            comment.user = request.user

            comment.save()

            context_dict['review'] = comment.review
            context_dict['rating'] = comment.rating
            context_dict['user'] = request.user.username

            return HttpResponseRedirect(reverse('cardetails', kwargs={'model_slug': model_slug}))
            #redirect(reverse('cardetails', kwargs={'model_slug': model_slug}))
        else:
            print(form.errors)

    context_dict['form'] = form
    context_dict['avgrate']=Review.objects.filter(post=car.ID).aggregate(Avg=Round(Avg('rating'),1))
    car.rating=context_dict['avgrate']['Avg']
    car.save()

    reviews_list = Review.objects.filter(post=car).order_by('-created_date')[:5]
    context_dict['all_reviews'] = reviews_list

    response = render(request, 'carride/cardetails.html', context=context_dict)
    print("bye")

    print(request.user)
    return response

def compare(request):
    context_dict ={}

    form = CompareForm()

    if request.method == 'POST':
        form = CompareForm(request.POST)
        if form.is_valid():

            form.save(commit = False)
            form.save(commit = False)

            try:
                car_1 = Vehicle.objects.get(ID=form.cleaned_data['ID1'])
                context_dict['car_1'] = car_1
            except Vehicle.DoesNotExist:
                context_dict['car_1'] = None

            try:
                car_2 = Vehicle.objects.get(ID=form.cleaned_data['ID2'])
                context_dict['car_2'] = car_2
            except Vehicle.DoesNotExist:
                context_dict['car_2'] = None
        
        else:

            print(form.errors)
            print('This ID does not exist')

    context_dict['form'] = form

    response = render(request, 'carride/compare.html', context_dict)
    return response

def sell(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)

    response=render(request, 'carride/sell.html', {'form': form})
    return response

def buy(request):

    car_list = Vehicle.objects.filter(forSale=True)
    paginator = Paginator(car_list, 2)
    page=request.GET.get('page',1)
    car_page=paginator.page(page)
    context_dict ={'car_list':car_page}    
    response = render(request, 'carride/buy.html', context=context_dict)
    return response

def rent(request):
    
    car_list = Vehicle.objects.filter(forSale=False)
    paginator = Paginator(car_list, 2)
    page=request.GET.get('page',1)
    car_page=paginator.page(page)
    context_dict ={'car_list':car_page}
    response = render(request, 'carride/rent.html', context=context_dict)
    return response
