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
def grok_chatbot(request):
    user_message = request.data.get("message", "")
    
    if not user_message:
        return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    grok_key = config("GROK_API_KEY", default="")
    
    # System prompt jo Grok ko batayega ke usne Moaz Ali ke AI assistant ke taur par behave karna hai
    system_prompt = """
    You are the premium, intelligent AI assistant for Moaz Ali, a talented Full Stack Developer, Software Engineer, and AI Engineer.
    Your job is to answer queries from potential clients, recruiters, and visitors on his portfolio website (moazali.com).
    
    Key Context about Moaz:
    - Tech Stack: Python, Django, Vue.js, React, AWS, PostgreSQL, SQL, Tailwind CSS.
    - Core Projects: 
      1. HireHarry.ai (AI-driven recruitment and candidate evaluation engine).
      2. TechHyves Systems (The software company he founded for digital transformation and business automation systems).
      3. Bakery POS System (High-performance application engineered with Vue.js frontend and Django REST Framework backend).
    - Status: Currently available for backend contracts, AI pipeline integrations, and custom software architecture work.
    
    Tone Guidelines:
    - Professional, helpful, concise, and futuristic minimal tech vibe.
    - If someone asks to schedule a meeting or contract him, encourage them to fill out the contact form on the page or connect via the WhatsApp widget.
    - Keep responses relatively brief (under 3-4 sentences max unless detailing a technical stack) so it fits nicely in a small chat window.
    """
    
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {grok_key}"
    }
    
    payload = {
    # Isko default stable core model par set karein
    "model": "grok-2-latest", 
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ],
    "temperature": 0.7
}
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            api_data = response.json()
            bot_reply = api_data["choices"][0]["message"]["content"]
            return Response({"reply": bot_reply}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch response from Grok"}, status=response.status_code)
            
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)