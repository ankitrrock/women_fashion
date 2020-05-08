from django.urls import path
from appmart import views as app


urlpatterns = [
	path('', app.index, name="index"),
	path('register/', app.registerPage, name="register"),
	path('login/', app.loginPage, name="login"),  
	path('logout/', app.logoutUser, name="logout"),
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


]