from django.urls import path
from .views import hompage,cources,authentication,cource_checkout


urlpatterns = [
    path('',hompage.index,name='index'),
    path('cource/<str:slug>',cources.courcesPage,name='courcepage'),
    path('signup/',authentication.signup,name='signup'), 
    path('login/',authentication.signin,name='login'), 
    path('logout/',authentication.signout,name='logout'), 
    path('checkout/<str:slug>',cource_checkout.checkout,name='checkout'), 
    path('verify_payment',cource_checkout.verifyPayment,name='verify_payment'), 
] 
