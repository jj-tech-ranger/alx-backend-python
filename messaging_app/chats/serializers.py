"""Serializers for the messaging application models."""
from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    
    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'first_name',
            'last_name', 'phone_number', 'role', 'created_at'
        ]
        read_only_fields = ['user_id', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message model with sender details."""
    
    sender = UserSerializer(read_only=True)
    sender_id = serializers.UUIDField(write_only=True)
    
    class Meta:
        model = Message
        fields = [
            'message_id', 'sender', 'sender_id', 'conversation',
            'message_body', 'sent_at'
        ]
        read_only_fields = ['message_id', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for Conversation model with nested messages and participants."""
    
    messages = MessageSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    participants_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Conversation
        fields = [
            'conversation_id', 'participants', 'participants_ids',
            'messages', 'created_at'
        ]
        read_only_fields = ['conversation_id', 'created_at']
    
    def create(self, validated_data):
        """Create a new conversation with participants."""
        participants_ids = validated_data.pop('participants_ids', [])
        conversation = Conversation.objects.create(**validated_data)
        
        if participants_ids:
            participants = User.objects.filter(user_id__in=participants_ids)
            conversation.participants.set(participants)
        
        return conversation
