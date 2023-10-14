# from django.conf import settings  
# from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    # path('main/', views.main, name='main'),
    # path('vocab/', views.vocab, name='vocab')
]