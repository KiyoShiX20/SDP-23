"""
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, "home.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

# get current time
from django.utils import timezone
from datetime import datetime
from django.utils.dateformat import DateFormat


# write fuction to get current time
def time(request):
    now = datetime.now()
    formatted_now = DateFormat(now).format('Y-m-d H:i:s')
# render time to index2.html
    return render(request, "home.html", {"insert_date": formatted_now})

#render the dictionary
def template_view(request):
    name = "Pikachu"
    rollno = 101
    marks = 100
    my_dict = {
        'name':name, 'rollno': rollno, 'marks': marks
    }
    return render(request, "home.html", {"dict": my_dict})

from django.shortcuts import render

from polls.models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')


def students(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'home.html', context)
    """

from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 



@login_required(login_url = 'login')
def home(request):
	return render (request,"home.html", context = {})





def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('login')
