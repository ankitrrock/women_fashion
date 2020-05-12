from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('loginPage')

	context = {'form': form}
	return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logout_django(request):
	logout(request)
	return redirect('loginPage')

@login_required(login_url='loginPage')
def index(request):
	return render(request,'index.html')


@login_required(login_url='loginPage')
def about(request):
	return render(request,'about.html')


@login_required(login_url='loginPage')
def checkout(request):
	return render(request,'checkout.html')


@login_required(login_url='loginPage')
def dresses(request):
	return render(request,'dresses.html')

@login_required(login_url='loginPage')
def faq(request):
	return render(request,'faq.html')


@login_required(login_url='loginPage')
def jeans(request):
	return render(request,'jeans.html')


@login_required(login_url='loginPage')
def mail(request):
	return render(request,'mail.html')


@login_required(login_url='loginPage')
def products(request):
	return render(request,'products.html')


@login_required(login_url='loginPage')
def salwars(request):
	return render(request,'salwars.html')


@login_required(login_url='loginPage')
def sandals(request):
	return render(request,'sandals.html')


@login_required(login_url='loginPage')
def sarees(request):
	return render(request,'sarees.html')


@login_required(login_url='loginPage')
def shirts(request):
	return render(request,'shirts.html')


@login_required(login_url='loginPage')
def shirtcodes(request):
	return render(request,'shirtcodes.html')


@login_required(login_url='loginPage')
def single(request):
	return render(request,'single.html')


@login_required(login_url='loginPage')
def skirts (request):
	return render(request,'skirts.html')


@login_required(login_url='loginPage')
def sweaters (request):
	return render(request,'sweaters.html')





