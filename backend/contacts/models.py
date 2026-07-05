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
    
class ChatbotKnowledge(models.Model):
    category = models.CharField(max_length=100, help_text="e.g., skills, projects, contact")
    keywords = models.TextField(help_text="Comma-separated keywords (e.g., python, django, backend)")
    response = models.TextField(help_text="The answer the bot will give.")

    def __str__(self):
        return f"{self.category} - {self.keywords[:30]}"

class UnansweredQuery(models.Model):
    query = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"New Query: {self.query[:50]}"