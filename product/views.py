from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('main')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main')
			else:
				messages.info(request, 'Username OR password is incorrect')

		
		
		return render(request, 'login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')
@login_required(login_url='login_data')
def main(request):
    
    return render(request,"dashboard.html")
@login_required(login_url='login')
def products(request):
       
    return render(request,"product.html")
@login_required(login_url='login')
def customer(request):
   
    return render(request,"customer.html")
@login_required(login_url='login')
def createOrder(request):
	return render(request, 'orderform.html')
@login_required(login_url='login')
def updateOrder(request):

	return render(request, 'orderform.html')
@login_required(login_url='login')
def deleteOrder(request):
	
	return render(request, 'delete.html')
