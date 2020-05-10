from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from appmart.forms import CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
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
	return render(request, 'registerPage', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('loginPage')

@login_required(login_url='loginPage')
def main(request):
	return render(request, "dashboard.html")

@login_required(login_url='loginPage')
def product(request):
	return render(request,"product.html")

@login_required(login_url='loginPage')
def customer(request):
	return render(request, "customer.html")

@login_required(login_url='loginPage')
def createOrder(request):
	return render(request, 'orderform.html')

@login_required(login_url='loginPage')
def updateOrder(request):

	return render(request, 'orderform.html')\

@login_required(login_url='loginPage')
def deleteOrder(request):
	return render(request, 'delete.html')
