# contacts/urls.py
from django.urls import path
from .views import contact_form_submit

urlpatterns = [
    path('submit/', contact_form_submit, name='contact-submit'),
]