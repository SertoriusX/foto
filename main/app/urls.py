
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.cards,name="home"),
    path('home/',views.cards,name="home"),
    path('detail/<int:card_id>/',views.detail,name="detail"),
]

