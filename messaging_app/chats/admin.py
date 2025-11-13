"""Django admin configuration for chats models."""
from django.contrib import admin
from .models import User, Conversation, Message


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model."""
    
    list_display = ('email', 'first_name', 'last_name', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('-created_at',)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Admin configuration for Conversation model."""
    
    list_display = ('conversation_id', 'created_at', 'get_participants_count')
    filter_horizontal = ('participants',)
    ordering = ('-created_at',)
    
    def get_participants_count(self, obj):
        """Return the number of participants in the conversation."""
        return obj.participants.count()
    get_participants_count.short_description = 'Participants'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin configuration for Message model."""
    
    list_display = ('message_id', 'sender', 'conversation', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('message_body', 'sender__email')
    ordering = ('-sent_at',)
