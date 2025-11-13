"""Django app configuration for chats application."""
from django.apps import AppConfig


class ChatsConfig(AppConfig):
    """Configuration class for the chats application."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chats'
