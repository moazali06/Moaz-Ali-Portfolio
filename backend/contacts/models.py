# contacts/models.py
from django.db import models

class ContactMessage(models.Model):
    # Yahan 'max_w_md' ko hata kar 'max_length' kar dein
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    message = models.TextField()
    budget= models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"