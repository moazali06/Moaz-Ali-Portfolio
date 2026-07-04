# contacts/urls.py
from django.urls import path
from .views import contact_form_submit,grok_chatbot

urlpatterns = [
    path('submit/', contact_form_submit, name='contact-submit'),
     path('chatbot/', grok_chatbot, name='chatbot'),

]