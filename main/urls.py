from unicodedata import name
from django.urls import path ,include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='main'


urlpatterns = [
    # path('',URLListView.as_view(),name='home'),
    path(r'^a/(?p<shortcode>[\w-]+)/$',URLListView.as_view(),name='home'),
    # path('hotel/',PropertyList.as_view(),name='property_list'),
    # path('hotel/<slug:slug>',PropertyDetail.as_view(),name='property_detail'),
    # path('create/',PropertyCreate.as_view(),name='property_create'),
    
    
    # # api
    # path('property/list',PropertyAPiList.as_view(),name='PropertyAPiList'),
    # path('property/list/<int:pk>',PropertyAPiDetail.as_view(),name='PropertyAPiDetail'),
]
