from django.contrib import admin
from .models import ContactMessage,ChatbotKnowledge, UnansweredQuery

admin.site.register(ContactMessage)

@admin.register(ChatbotKnowledge)
class ChatbotKnowledgeAdmin(admin.ModelAdmin):
    list_display = ('category', 'keywords')
    search_fields = ('category', 'keywords', 'response')

@admin.register(UnansweredQuery)
class UnansweredQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'timestamp', 'is_resolved')
    list_filter = ('is_resolved',)