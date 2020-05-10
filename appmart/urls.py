from django.urls import path
from appmart import views as app


urlpatterns = [
	path('', app.index, name="index"),
	path('registerPage/', app.registerPage, name="registerPage"),
	path('loginPage/', app.loginPage, name="loginPage"),
	path('logout_django/', app.logout_django, name="logout_django"),
	path('about', app.about, name="about"),
	path('checkout', app.checkout, name="checkout"),
	path('dresses', app.dresses, name="dresses"),
	path('faq', app.faq, name="faq"),
	path('jeans', app.jeans, name="jeans"),
	path('mail', app.mail, name="mail"),
	path('products', app.products, name="products"),
	path('salwars', app.salwars, name="salwars"),
	path('sandals', app.sandals, name="sandals"),
	path('sarees', app.sarees, name="sarees"),
	path('shirts', app.shirts, name="shirts"),
	path('shirtcodes', app.shirtcodes, name="shirtcodes"),
	path('single', app.single, name="single"),
	path('skirts', app.skirts, name="skirts"),
	path('sweaters', app.sweaters, name="sweaters"),
	path('ankit', app.ankit, name="ankit"),


]