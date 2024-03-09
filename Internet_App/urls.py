from django.contrib import admin
from django.urls import path
from Internet_App import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('service/',views.service),
    path('price/',views.price),
    path('contact/',views.contact),
    path('welcome/',views.welcome_page, name='welcome'),
    path('plans/',views.plans, name='plans'),
    path('userlogout/',views.userlogout),
    path('update_profile/',views.profile),
    path('buy_plan_1099/',views.buy_1099),
    path('buy_plan_1599/',views.buy_1599),
    path('buy_plan_2099/',views.buy_2099),
    path('complaint/', views.complaint,  name='complaint'),
    path('customer_det/', views.customer_det),
    path('membar_page/', views.membar_page),
    path('status_update/<int:id>', views.status_update),
    path('sub/',views.subscribe, name='submit'),





]
