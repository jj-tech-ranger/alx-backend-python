tests.py"""Test cases for the chats application."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Conversation, Message
import uuid

User = get_user_model()


class UserModelTest(TestCase):
    """Test cases for the User model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            role='guest'
        )
    
    def test_user_creation(self):
        """Test that a user can be created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.role, 'guest')
        self.assertTrue(isinstance(self.user.user_id, uuid.UUID))
    
    def test_user_string_representation(self):
        """Test the string representation of the user."""
        expected = f"{self.user.email} ({self.user.role})"
        self.assertEqual(str(self.user), expected)


class ConversationModelTest(TestCase):
    """Test cases for the Conversation model."""
    
    def setUp(self):
        """Set up test data."""
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='pass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='pass123'
        )
        self.conversation = Conversation.objects.create()
        self.conversation.participants.add(self.user1, self.user2)
    
    def test_conversation_creation(self):
        """Test that a conversation can be created."""
        self.assertTrue(isinstance(self.conversation.conversation_id, uuid.UUID))
        self.assertEqual(self.conversation.participants.count(), 2)
    
    def test_conversation_participants(self):
        """Test the many-to-many relationship with participants."""
        self.assertIn(self.user1, self.conversation.participants.all())
        self.assertIn(self.user2, self.conversation.participants.all())


class MessageModelTest(TestCase):
    """Test cases for the Message model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.conversation = Conversation.objects.create()
        self.conversation.participants.add(self.user)
        self.message = Message.objects.create(
            sender=self.user,
            conversation=self.conversation,
            message_body='Test message content'
        )
    
    def test_message_creation(self):
        """Test that a message can be created."""
        self.assertTrue(isinstance(self.message.message_id, uuid.UUID))
        self.assertEqual(self.message.sender, self.user)
        self.assertEqual(self.message.conversation, self.conversation)
        self.assertEqual(self.message.message_body, 'Test message content')
    
    def test_message_string_representation(self):
        """Test the string representation of the message."""
        expected = f"Message from {self.user.email} at {self.message.sent_at}"
        self.assertEqual(str(self.message), expected)
    
    def test_message_relationships(self):
        """Test foreign key relationships."""
        self.assertEqual(self.message.sender.email, 'test@example.com')
        self.assertIn(self.message, self.conversation.messages.all())
