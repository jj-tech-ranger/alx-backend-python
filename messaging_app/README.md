# Messaging App - Django REST Framework Project

## Project Overview

A robust RESTful API messaging application built with Django and Django REST Framework. This project implements a complete messaging system with users, conversations, and messages, following industry best practices for API design and database modeling.

## Features

- **Custom User Model**: Extended Django's AbstractUser with additional fields (phone_number, role)
- **UUID Primary Keys**: All models use UUID for primary keys with proper indexing
- **RESTful API Endpoints**: Full CRUD operations for Users, Conversations, and Messages
- **Nested Relationships**: Conversations include participants and messages
- **Django Admin Integration**: Fully configured admin interface for all models
- **Optimized Queries**: Uses select_related and prefetch_related for performance

## Project Structure

```
messaging_app/
├── manage.py
├── messaging_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── chats/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## Database Schema

### User Model
- `user_id` (UUID, Primary Key, Indexed)
- `username`, `email`, `first_name`, `last_name` (from AbstractUser)
- `phone_number` (VARCHAR, nullable)
- `role` (ENUM: guest/host/admin)
- `created_at` (TIMESTAMP)

### Conversation Model
- `conversation_id` (UUID, Primary Key, Indexed)
- `participants` (ManyToMany relationship with User)
- `created_at` (TIMESTAMP)

### Message Model
- `message_id` (UUID, Primary Key, Indexed)
- `sender` (ForeignKey to User)
- `conversation` (ForeignKey to Conversation)
- `message_body` (TEXT)
- `sent_at` (TIMESTAMP)

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jj-tech-ranger/alx-backend-python.git
cd alx-backend-python/messaging_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

All endpoints are accessible under `/api/`:

### Users
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{user_id}/` - Retrieve a specific user
- `PUT /api/users/{user_id}/` - Update a user
- `DELETE /api/users/{user_id}/` - Delete a user

### Conversations
- `GET /api/conversations/` - List all conversations
- `POST /api/conversations/` - Create a new conversation
- `GET /api/conversations/{conversation_id}/` - Retrieve a conversation with messages
- `PUT /api/conversations/{conversation_id}/` - Update a conversation
- `DELETE /api/conversations/{conversation_id}/` - Delete a conversation
- `POST /api/conversations/{conversation_id}/add_message/` - Add a message to a conversation

### Messages
- `GET /api/messages/` - List all messages
- `GET /api/messages/?conversation_id={uuid}` - Filter messages by conversation
- `POST /api/messages/` - Create a new message
- `GET /api/messages/{message_id}/` - Retrieve a specific message
- `PUT /api/messages/{message_id}/` - Update a message
- `DELETE /api/messages/{message_id}/` - Delete a message

## Testing

### Using Django Shell
```bash
python manage.py shell
```

```python
from chats.models import User, Conversation, Message

# Create a user
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123',
    role='guest'
)

# Create a conversation
conversation = Conversation.objects.create()
conversation.participants.add(user)

# Create a message
message = Message.objects.create(
    sender=user,
    conversation=conversation,
    message_body='Hello, this is a test message!'
)
```

### Using API Testing Tools

**With curl:**
```bash
# List all conversations
curl http://localhost:8000/api/conversations/

# Create a new conversation
curl -X POST http://localhost:8000/api/conversations/ \
  -H "Content-Type: application/json" \
  -d '{"participants_ids": ["user-uuid-here"]}'
```

**With Postman or similar tools:**
1. Import the base URL: `http://localhost:8000/api/`
2. Test each endpoint with appropriate request methods
3. Use the browsable API by visiting endpoints in a web browser

## Admin Interface

Access the Django admin at: `http://localhost:8000/admin/`

Features:
- User management with role filtering
- Conversation management with participant counts
- Message management with sender and conversation details

## Configuration

### Settings Highlights
- **Database**: SQLite (default, configurable in `settings.py`)
- **Authentication**: Custom User model (`chats.User`)
- **REST Framework**: Pagination enabled (10 items per page)
- **Time Zone**: UTC

## Project Requirements Met

✅ Django project scaffolding with industry-standard structure
✅ Custom User model extending AbstractUser
✅ UUID primary keys for all models
✅ Proper database relationships (ForeignKey, ManyToMany)
✅ Database indexes on key fields
✅ Django REST Framework integration
✅ Serializers with nested relationships
✅ ViewSets for clean API endpoints
✅ DefaultRouter for automatic URL routing
✅ Django Admin configuration

## Technologies Used

- **Django 4.x**: Web framework
- **Django REST Framework**: API toolkit
- **SQLite**: Database (development)
- **Python 3.x**: Programming language

## Next Steps

- Add authentication (JWT/Token-based)
- Implement permissions and access control
- Add pagination and filtering
- Write unit tests
- Add API documentation (Swagger/OpenAPI)
- Deploy to production

## Author

Project created as part of the ALX Backend Python specialization.

## License

This project is for educational purposes.
