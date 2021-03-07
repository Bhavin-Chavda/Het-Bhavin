from django.contrib import admin
from django.urls import path,include

from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('workout',views.workout,name='workout'),
    path('endurance',views.endurance,name='endurance'),
    path('strength_training',views.strength_training,name='strength_training'),
    path('cross_training',views.cross_training,name='cross_training'),
    path('hitt',views.hitt,name='hitt'),
    path('core_strength',views.core_strength,name='core_strength'),
    path('resistance',views.resistance,name='resistance'),
]