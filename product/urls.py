from django.urls import path
from product import views as pt


urlpatterns = [
    path('registerPage/', pt.registerPage, name="registerPage"),
    path('loginPage/', pt.loginPage, name="login_Page"),
    path('logoutUser/', pt.logoutUser, name="logoutUser"),
    path("", pt.main, name='main'),
    path("product/", pt.product, name='product'),
    path('customer/', pt.customer, name="customer"),
    path('create_order/', pt.createOrder, name="create_order"),
    path('update_order/', pt.updateOrder, name="update_order"),
    path('delete_order//', pt.deleteOrder, name="delete_order"),
    
]   
