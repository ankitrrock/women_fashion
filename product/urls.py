from django.urls import path
from product import views as pt


urlpatterns = [
    path('register/', pt.registerPage, name="register"),
	path('login/', pt.loginPage, name="login_data"),  
	path('logout/', pt.logout, name="logout"),
    path("",pt.main,name='main'),
    path("products/",pt.products,name='products'),
    path('customer/', pt.customer, name="customer"),
    path('create_order/', pt.createOrder, name="create_order"),
    path('update_order/', pt.updateOrder, name="update_order"),
    path('delete_order//', pt.deleteOrder, name="delete_order"),
    
]   
