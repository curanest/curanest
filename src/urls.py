from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from prof import views as profviews
#from prof import HospitalProfileView, SizesView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/',include("prof.api.urls", namespace='api')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^query/$', profviews.query, name='query'),
    url(r'^aboutus/$', profviews.aboutus, name='aboutus'),
    url(r'^termsandconditions/$', profviews.tandc, name='tandc'),
    url(r'^agentquery/$', profviews.agentquery, name='agent_query'),
    url(r'^query/(?P<hospital>\w+)/$', profviews.query, name='query'),
    #url(r'^query/(?P<hospital>\w+)/', profviews.query, name='query_o'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),    
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),    
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'), 
    url(r'^$', profviews.dashboard, name='dashboard'), 
    url(r'^edit/', profviews.edit, name='edit'),
    url(r'^mail/', profviews.sendmail_one, name='sendmail_one'),
    #url(r'^dashboard/', profviews.dashboard, name='dashboard'),
    url(r'^register/(?P<usertype>\w+)/$', profviews.register, name='register'),
    url(r'^ratings_vote/$', profviews.ratings_vote, name='ratings_vote'),
    url(r'^contactus/$', profviews.contact_us, name='contactus'),
    url(r'^hospitals/$', profviews.show_hospitals, name='hospitals'),
    url(r'^hospitals/(?P<username>\w+)/$', profviews.hospital_details, name='hospital_details'),
    url(r'^hospitalsview/(?P<hospital>\w*)/$', profviews.HospitalProfileView.as_view(template_name='home.html'), name='hospital_view'),
    #url(r'^sizes$', profviews.SizesView.as_view(), name='sizes'),
    # url(r'^', include(auth_urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    #url(r'^ratings/', include('ratings.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 
