# from django.conf import settings  
# from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('vocabulary/', views.vocabulary, name='vocabulary')
]