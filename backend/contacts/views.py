from django.conf import settings
from django.core.mail import send_mail
# ==========================================
# FIX: csrf_exempt ko import karein
# ==========================================
from django.views.decorators.csrf import csrf_exempt 

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContactMessageSerializer
from decouple import config
from .models import ChatbotKnowledge, UnansweredQuery
import requests









@csrf_exempt
@api_view(["POST"])
def contact_form_submit(request):
    serializer = ContactMessageSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        # ---------------------------
        # Email to Admin
        # ---------------------------
        admin_subject = f"New Portfolio Inquiry - {contact.name}"
        admin_message = f"""
A new portfolio contact form has been submitted.

Name:
{contact.name}

Email:
{contact.email}

Budget:
{contact.budget}

Message:
{contact.message}
"""

        send_mail(
            subject=admin_subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        # ---------------------------
        # Confirmation Email to User
        # ---------------------------
        user_subject = "Thank you for contacting Moaz Ali"
        user_message = f"""
Hi {contact.name},

Thank you for reaching out.

I have successfully received your message and will review it shortly.

----------------------------------
Your Submission

Name:
{contact.name}

Email:
{contact.email}

Budget:
{contact.budget}

Message:
{contact.message}
----------------------------------

I will get back to you as soon as possible.

Regards,
Moaz Ali
Full Stack Python Developer
"""

        send_mail(
            subject=user_subject,
            message=user_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False,
        )

        return Response(
            {
                "success": True,
                "message": "Message received successfully!"
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.conf import settings
from django.core.mail import send_mail
# ==========================================
# FIX: csrf_exempt ko import karein
# ==========================================
from django.views.decorators.csrf import csrf_exempt 

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContactMessageSerializer
from decouple import config
import requests









@csrf_exempt
@api_view(["POST"])
def contact_form_submit(request):
    serializer = ContactMessageSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        # ---------------------------
        # Email to Admin
        # ---------------------------
        admin_subject = f"New Portfolio Inquiry - {contact.name}"
        admin_message = f"""
A new portfolio contact form has been submitted.

Name:
{contact.name}

Email:
{contact.email}

Budget:
{contact.budget}

Message:
{contact.message}
"""

        send_mail(
            subject=admin_subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        # ---------------------------
        # Confirmation Email to User
        # ---------------------------
        user_subject = "Thank you for contacting Moaz Ali"
        user_message = f"""
Hi {contact.name},

Thank you for reaching out.

I have successfully received your message and will review it shortly.

----------------------------------
Your Submission

Name:
{contact.name}

Email:
{contact.email}

Budget:
{contact.budget}

Message:
{contact.message}
----------------------------------

I will get back to you as soon as possible.

Regards,
Moaz Ali
Full Stack Python Developer
"""

        send_mail(
            subject=user_subject,
            message=user_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False,
        )

        return Response(
            {
                "success": True,
                "message": "Message received successfully!"
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
def grok_chatbot(request): # URL path change na karna pare isliye naam yahi rakha hai
    user_message = request.data.get("message", "").strip().lower()
    
    if not user_message:
        return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    # Default greeting response handler
    if user_message in ['hi', 'hello', 'hey', 'aoa', 'assalam o alaikum']:
        reply = "Hi! I'm Moaz's smart assistant. Ask me about his tech stack, projects, experience, or how to contact him!"
        return Response({"reply": reply}, status=status.HTTP_200_OK)

    # Database se saara knowledge fetch karein
    knowledge_base = ChatbotKnowledge.objects.all()
    best_match = None
    highest_score = 0

    # Simple Keyword Score Matching Engine
    for entry in knowledge_base:
        keywords = [k.strip().lower() for k in entry.keywords.split(',')]
        score = 0
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', user_message):
                score += 1
        
        if score > highest_score:
            highest_score = score
            best_match = entry

    # Agar koi match mil gaya
    if highest_score > 0 and best_match:
        return Response({"reply": best_match.response}, status=status.HTTP_200_OK)
    
    # AGAR KOI MATCH NAHI MILA -> Auto Learning Process Trigger
    # Yeh query database mein chali jayegi taake aap admin se iska answer add kar sakein
    UnansweredQuery.objects.create(query=user_message)
    
    fallback_reply = "I'm still learning about that specific part of Moaz's experience. I have logged your question for Moaz to review! Meanwhile, you can drop a message via the WhatsApp widget or the contact form above."
    return Response({"reply": fallback_reply}, status=status.HTTP_200_OK)