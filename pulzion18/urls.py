"""pulzion18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from registrations import views as RegistrationViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', RegistrationViews.homePage, name='homePage'),
    url(r'^register/', include('registrations.urls'), name='RegistrationPage'),
    url(r'^participants/$', RegistrationViews.getParticipantList, name='ParticipantList'),
    url(r'certify(?P<receiptNumber>[0-9]+)/$', RegistrationViews.postToCertificateList, name='AddToCertificateList'),
    url(r'event(?P<receiptNumber>[0-9]+)/$', RegistrationViews.postToEventList, name='AddToEventList'),
    url(r'^(?P<event>[A-Za-z_]+_list)/$', RegistrationViews.getEventParticipants, name='EventParticipantsList'),
    url(r'^certificate/', RegistrationViews.certificateList, name='CertificationPage'),
    url(r'^events/',RegistrationViews.eventsList, name='EventsPage')
]
