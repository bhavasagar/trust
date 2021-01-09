from django.urls import path
from . import views
from django.conf.urls import (handler400, handler403, handler404)
# from allauth.account.views import SignupView
from .views import (  
    Home,
    Blog_page,
    Obanna,
    Events_page,
    About,
    Gallery_page,
    Blogs,
)

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),      
    path('blog/<int:pk>/', Blog_page.as_view(), name='blog-detail'),      
    path('gallery/', Gallery_page.as_view(), name='gallery'),
    path('blogs/', Blogs.as_view(), name='blogs'),      
    path('events/', Events_page.as_view(), name='events'),
    path('obanna/', Obanna, name='obanna'),      
    path('about/', About, name='about'), 
]