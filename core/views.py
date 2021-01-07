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
from .models import Gallery, Blog, Event, Carousal
from django.db.models.functions import ( ExtractDay, ExtractHour, ExtractMinute, ExtractMonth, ExtractSecond, ExtractWeek, ExtractWeekDay, ExtractYear )
from django.utils.html import format_html

class Home(View):
    template_name='home.html'
    def get(self, *args, **kwargs):
        carousal = Carousal.objects.all()
        gallery = Gallery.objects.all()
        context={ 'carousal':carousal,'gallery':gallery }        
        return render(self.request,self.template_name,context=context)

class Blog_page(View):
    template_name='blog.html'
    def get(self, *args, **kwargs):
        blog = Blog.objects.get(pk=1)
        context={ 'blog':blog}        
        return render(self.request,self.template_name,context=context)

class Events_page(View):
    template_name='events.html'
    def get(self, *args, **kwargs):
        events = Event.objects.all()
        context={ 'events':events}        
        return render(self.request,self.template_name,context=context)

def Obanna(request):
    return render(request,'obanna.html')

def About(request):
    return render(request,'about.html')