from django.shortcuts import render,redirect
from .forms import SignUpForm, PostForm

from django.contrib.auth import authenticate
from django.contrib import messages

def feed(request):
    return render(request, 'feed.html')

#ignore this
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            return redirect('feed')
#    else:
    #    form = Postform()
    #return render(request, 'post.html',{'form':form})

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return redirect('feed')
    else:
        form = Postform()
    return render(request, 'post.html',{'form':form})

def home(request):
    return render(request,'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  #creates bound version of the form wiht our POST data.
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:

        form = SignUpForm()
    return render(request,'sign_up.html', {'form':form})
