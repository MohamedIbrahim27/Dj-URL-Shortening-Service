from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView ,DetailView ,CreateView
from.models import URL
from django.views import View
# Create your views here.

# class URLListView(ListView):
#     model = URL
#     context_object_name='all_url'
#     template_name = "main/url.html"


class URLListView(View):
    def get(self,request,*args, **kwargs):
        HttpResponse("hello")