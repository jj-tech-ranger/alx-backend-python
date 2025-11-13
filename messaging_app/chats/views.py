"""ViewSets for the messaging application API endpoints."""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model operations."""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for Conversation model with nested message creation."""
    
    queryset = Conversation.objects.prefetch_related(
        'participants', 'messages', 'messages__sender'
    ).all()
    serializer_class = ConversationSerializer
    lookup_field = 'conversation_id'
    
    @action(detail=True, methods=['post'])
    def add_message(self, request, conversation_id=None):
        """Add a message to a conversation."""
        conversation = self.get_object()
        message_data = request.data.copy()
        message_data['conversation'] = conversation.conversation_id
        
        serializer = MessageSerializer(data=message_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for Message model operations."""
    
    queryset = Message.objects.select_related('sender', 'conversation').all()
    serializer_class = MessageSerializer
    lookup_field = 'message_id'
    
    def get_queryset(self):
        """Filter messages by conversation if provided."""
        queryset = super().get_queryset()
        conversation_id = self.request.query_params.get('conversation_id')
        
        if conversation_id:
            queryset = queryset.filter(conversation__conversation_id=conversation_id)
        
        return queryset
    
    def perform_create(self, serializer):
        """Create a message with the sender from request data."""
        sender_id = self.request.data.get('sender_id')
        if sender_id:
            serializer.save(sender_id=sender_id)
        else:
            serializer.save()
