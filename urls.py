from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('index.html', views.index, name='home'),
    path('Menu.html', views.menu, name='menu'),
    path('Constructor_Pizza.html', views.constructor, name='constructor'),
    path('Registration.html', views.registration, name='registration'),
    path('about.html', views.about, name='about'),
    path('login_page', views.login_page, name='login'),
    path('success', views.success, name='success'),
    path('pizza with anchous.html', views.anchous, name='anchous'),
    path('Pizza in conus form.html', views.conus, name='conus'),
    path('Closed Pizza.html', views.close_pizza, name='close_pizza'),
    path('Fast pizza.html', views.fast_pizza, name='fast_pizza'),
    path('Fruit Pizza.html', views.fruit_pizza, name='fruit_pizza'),
    path('Potato `s pizza.html', views.potato_pizza, name='potato_pizza'),
]
