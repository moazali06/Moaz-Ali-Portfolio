from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContactMessageSerializer


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
https://moazali.com
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