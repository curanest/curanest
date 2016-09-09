from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	ContactUsCreateAPIView,
    ContactUsListAPIView,
    ContactUsUpdateAPIView,
    ContactUsDeleteAPIView,
    ContactUsRetrieveAPIView,
    AgentQueryCreateAPIView,
# <<<<<<< HEAD
#     #AgentProfileCreateAPIView
# =======
#     AgentProfileCreateAPIView
# >>>>>>> ef57d6dfc36652db4fb58388a8d5887316b505f7
	)

urlpatterns = [
    url(r'^$',ContactUsListAPIView.as_view(), name='list'),
    url(r'^contactus/create/$',ContactUsCreateAPIView.as_view(), name='create-contactus'),
    url(r'^agentquery/create/$',AgentQueryCreateAPIView.as_view(), name='create-query'),
#<<<<<<< HEAD
    #url(r'^agentprofile/create/$',AgentProfileCreateAPIView.as_view(), name='create-agentprofile'),
# =======
#     url(r'^agentprofile/create/$',AgentProfileCreateAPIView.as_view(), name='create-profile'),
# >>>>>>> ef57d6dfc36652db4fb58388a8d5887316b505f7
    url(r'^(?P<pk>[\w-]+)/$',ContactUsRetrieveAPIView.as_view(), name='detail-list'),
    url(r'^(?P<pk>[\w-]+)/edit$',ContactUsUpdateAPIView.as_view(), name='update-list'),
    url(r'^(?P<pk>[\w-]+)/delete$',ContactUsDeleteAPIView.as_view(), name='delete-list'),
]
