from django.conf.urls import url
from registrations import views as RegistrationViews

urlpatterns = [
    url(r'^$', RegistrationViews.getRegistrationForm, name='RegistrationForm'),
    url(r'^done/$', RegistrationViews.registered, name='registered'),
]