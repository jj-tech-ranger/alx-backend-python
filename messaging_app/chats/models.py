"""Database models for the messaging application."""
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model extending AbstractUser with additional fields."""
    
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=[
            ('guest', 'Guest'),
            ('host', 'Host'),
            ('admin', 'Admin'),
        ],
        default='guest'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email']),
        ]
    
    def __str__(self):
        return f"{self.email} ({self.role})"


class Conversation(models.Model):
    """Model representing a conversation between users."""
    
    conversation_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    participants = models.ManyToManyField(
        User,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'conversations'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Conversation {self.conversation_id}"


class Message(models.Model):
    """Model representing a message in a conversation."""
    
    message_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'messages'
        ordering = ['-sent_at']
        indexes = [
            models.Index(fields=['sender']),
            models.Index(fields=['conversation']),
        ]
    
    def __str__(self):
        return f"Message from {self.sender.email} at {self.sent_at}"
