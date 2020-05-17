from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from appmart.forms import CreateUserForm
from product.forms import TagForm, ColorForm, SizeForm, ProductForm

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
	return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginPage')

@login_required(login_url='loginPage')
def main(request):
	return render(request, "dashboard.html")

@login_required(login_url='loginPage')
def product(request):
	if request.method == 'POST':
		tagform = TagForm(request.POST)
		colorform = ColorForm(request.POST)
		sizeform = SizeForm(request.POST)
		productform = ProductForm(request.POST)
		if productform.is_valid():
			productform.save()
			messages.success(request, 'product data added')
			return HttpResponseRedirect(reverse('product'))
		elif colorform.is_valid():
			colorform.save()
			messages.success(request, 'product color added')
			return HttpResponseRedirect(reverse('product'))
		elif sizeform.is_valid():
			sizeform.save()
			messages.success(request, 'product size added')
			return HttpResponseRedirect(reverse('product'))
		elif tagform.is_valid():
			tagform.save()
			messages.success(request, 'product tag added')
			return HttpResponseRedirect(reverse('product'))
		else:
			messages.success(request, 'please fill relevant data')
			return HttpResponseRedirect(reverse('product'))
	else:
		tagform = TagForm()
		colorform = ColorForm()
		sizeform = SizeForm()
		productform = ProductForm()
	messages.success(request, 'Add the element')
	return render(request, 'product.html', {
		'tagform': tagform,
		'colorform': colorform,
		'sizeform': sizeform,
		'productform': productform,

	})

@login_required(login_url='loginPage')
def customer(request):
	return render(request, "customer.html")

@login_required(login_url='loginPage')
def createOrder(request):
	return render(request, "orderform.html")

@login_required(login_url='loginPage')
def updateOrder(request):

	return render(request, "orderform.html")

@login_required(login_url='loginPage')
def deleteOrder(request):
	return render(request, 'delete.html')
