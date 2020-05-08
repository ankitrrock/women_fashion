from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('', views.index, name="index"),
	path('about', views.about, name="about"),
	path('checkout', views.checkout, name="checkout"),
	path('dresses', views.dresses, name="dresses"),
	path('faq', views.faq, name="faq"),
	path('jeans', views.jeans, name="jeans"),
	path('mail', views.mail, name="mail"),
	path('products', views.products, name="products"),
	path('salwars', views.salwars, name="salwars"),
	path('sandals', views.sandals, name="sandals"),
	path('sarees', views.sarees, name="sarees"),
	path('shirts', views.shirts, name="shirts"),
	path('shirtcodes', views.shirtcodes, name="shirtcodes"),
	path('single', views.single, name="single"),
	path('skirts', views.skirts, name="skirts"),
	path('sweaters', views.sweaters, name="sweaters"),


]