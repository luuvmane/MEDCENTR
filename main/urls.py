from django.urls import path
from . import views
from main.apps import MainConfig
from main.views import IndexView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),

]
