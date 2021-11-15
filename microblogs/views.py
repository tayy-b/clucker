from django.shortcuts import redirect, render
# from django.http import HttpResponse
from .forms import LogInForm, SignUpForm, PostForm
from .models import User
from django.contrib.auth import authenticate,login, logout, get_user_model
from django.contrib import messages
from django.utils.timezone import datetime

# Create your views here.

#FEED view: displays a post
def feed(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                # username = request.user.username
                # print(username)
                post = form.save(request)
            time = datetime.now()
            print (time)
            # print (user)
            # print(list(user))
            return redirect('feed')
    else:
        form=PostForm()
    return render(request, 'post.html',  {'form': form})



#Home view - first page:
def home(request):
    # response = HttpResponse("Welcome to clucker!")
    return render(request, 'home.html')


#Sign up view: when you click sign_up:
def sign_up(request):
    # response = HttpResponse("Welcome to clucker!")
    if request.method == 'POST':   #if the request is a POST request, make a form with the post data
        form = SignUpForm(request.POST)   #form with post data => this makes a bounded form.
        if form.is_valid():    #if valid-> save the form and refirect to the url feed.
            user = form.save()       #FORM'S SAVE METHOD - Create user object through Forms.py, saved as variable "user"
            login(request, user)
            return redirect('feed')
    else:                           #else its a GET request
        form = SignUpForm()         #create a template form
    return render(request, 'sign_up.html',  {'form': form})


#Log in view: when you click log_in:
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})



#Log out view:
def log_out(request):
    logout(request)
    return redirect('home')


#USER LIST VIEW - Exercise 4.1
def user_list(request):
    #userList =User.objects.values() or all()
    User = get_user_model()
    list = User.objects.all()
    return render(request, 'user_list.html', {"list":list})


def show_user(request, user_id):
    User = get_user_model()
    list = User.objects.filter(id=user_id)
    # user = User.objects.values_list('id', flat=True)
    # first_user = User.objects.all()[user_id-1]
    # print(first_user)
    # print(list)
    return render(request, 'show_user.html', {"list":list})



def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                # username = request.user.username
                # print(username)
                post = form.save(request)
                time = datetime.now()
                print (time)
                # print (user)
                # print(list(user))
                return redirect('new_post')
    else:
        form=PostForm()
    return render(request, 'new_post.html',  {'form': form})
