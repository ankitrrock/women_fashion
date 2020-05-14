from django.shortcuts import render, redirect
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


# noinspection SpellCheckingInspection
@login_required(login_url='loginPage')
def product(request):
	tagform = TagForm()
	colorform = ColorForm()
	sizeform = SizeForm()
	productform = ProductForm()
	if request.method == 'POST':
		tagform = TagForm(request.POST)
		colorform = ColorForm(request.POST)
		sizeform = SizeForm(request.POST)
		productform = ProductForm(request.POST)
		if tagform.is_valid():
			tagform.save()
			tag = tagform.cleaned_data.get('tag')
			messages.success(request, 'successfully added ')
			return redirect('product')

		elif colorform.is_valid():
			colorform.save()
			color = colorform.cleaned_data.get('color')
			messages.success(request, 'color successfully added')
			return redirect('product')
		elif sizeform.is_valid():
			sizeform.save()
			size = sizeform.cleaned_data.get('size')
			messages.success(request, 'size successfully added')
			return redirect('product')
		elif productform.is_valid():
			productform.save()
			productform = productform.cleaned_data.get('product')
			messages.success(request, 'product successfully added')
			return redirect('product')
	context = {'tagform': tagform, 'colorform': sizeform, 'sizeform': sizeform, 'productform': productform}
	return render(request, "product.html", context)


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
