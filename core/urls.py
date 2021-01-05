from django.urls import path
from . import views
from django.conf.urls import (handler400, handler403, handler404)
# from allauth.account.views import SignupView
from .views import (  
    Home,
)

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),      
]