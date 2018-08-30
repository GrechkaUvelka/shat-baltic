from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.send, name="send"),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('robots.txt', views.robots, name="robots.txt"),
]
