from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils import timezone
# from .models import History, UserProfile, Transaction, Paytm_history, GoldGame, SilverGame, DiamondGame, OtherGame, withdraw_requests, Contact, Carousal, RedEnvelope, Carousal1, Carousal2, Carousal3, Notifications, Home_description
import random
from django.shortcuts import reverse
import string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import smtplib
from django.core.paginator import Paginator
from email.message import EmailMessage
from datetime import datetime, timedelta
from django.db.models import Q
from .models import Gallery, Blog, Event, Carousal, TrustMember
from django.db.models.functions import ( ExtractDay, ExtractHour, ExtractMinute, ExtractMonth, ExtractSecond, ExtractWeek, ExtractWeekDay, ExtractYear )
from django.utils.html import format_html

class Home(View):
    template_name='home.html'
    def get(self, *args, **kwargs):
        carousal = Carousal.objects.all()
        gallery = Gallery.objects.all()
        events = Event.objects.filter(status="O")
        blogs = Blog.objects.filter(homepage_display=True)
        context={ 'carousal':carousal,'gallery':gallery, 'events':events, 'blogs':blogs }        
        return render(self.request,self.template_name,context=context)
    def post(self, *args, **kwargs):
        name = self.request.POST.get('name')
        email =  self.request.POST.get('email')
        phone =  self.request.POST.get('phone')
        address =  self.request.POST.get('address')
        TrustMember.objects.create(name=name,email=email,phone=phone,address=address)
        return redirect('core:home')

class Blog_page(View):
    template_name='blog.html'
    def get(self, *args, **kwargs):
        blog = Blog.objects.get(pk=kwargs['pk'])
        blogs = Blog.objects.all().exclude(pk=kwargs['pk']).order_by('-id')
        context={ 'blog':blog,'blogs':blogs}        
        return render(self.request,self.template_name,context=context)

class Blogs(View):
    template_name='allblogs.html'
    def get(self, *args, **kwargs):        
        blogs = Blog.objects.all().order_by('-id')
        context={'blogs':blogs}        
        return render(self.request,self.template_name,context=context)

class Gallery_page(View):
    template_name='gallery.html'
    def get(self, *args, **kwargs):
        count = Gallery.objects.all().count()
        images1 = Gallery.objects.all().order_by('-id')[0:int(count/4)]
        images2 = Gallery.objects.all().order_by('-id')[int(count/4)+1:int(count/2)]
        images3 = Gallery.objects.all().order_by('-id')[int(count/2)+1:3*int(count/4)]
        images4 = Gallery.objects.all().order_by('-id')[3*int(count/4):int(count)]
        context={ 'images1':images1,'images2':images2,'images3':images3,'images4':images4}        
        return render(self.request,self.template_name,context=context)

class Events_page(View):
    template_name='events.html'
    def get(self, *args, **kwargs):
        uevents = Event.objects.filter(status="U")
        oevents = Event.objects.filter(status="O")
        cevents = Event.objects.filter(status="c")
        context={ 'uevents':uevents,'cevents':cevents,'oevents':oevents}        
        return render(self.request,self.template_name,context=context)

def Obanna(request):
    return render(request,'obanna.html')

def About(request):
    return render(request,'about.html')