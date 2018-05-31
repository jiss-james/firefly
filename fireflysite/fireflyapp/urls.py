from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userhome', views.userhome, name='userhome'),
    path('account_settings', views.user_account_settings, name='account_settings'),
    path('results/$', views.results, name='results')

]
