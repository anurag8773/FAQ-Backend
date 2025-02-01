# FAQ API

The **FAQ API** is a RESTful API service designed for managing frequently asked questions (FAQs) with multi-language translation support. It includes features such as CRUD operations, language-specific FAQ retrieval, caching for optimized performance, and integration with WYSIWYG editors for managing content.

This API can store and manage FAQs in multiple languages, including English, Hindi, and Bengali. Users can create, update, and delete FAQs while leveraging caching mechanisms (Redis) for fast access to frequently requested data.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
- [File Structure](#file-structure)
- [API Usage Examples](#api-usage-examples)

## Features
- **Multi-language Support**: Fetch FAQs in different languages like English, Hindi, and Bengali.
- **Operations**: Create, read, and update FAQ entries with language-specific support.
- **Caching**: Redis integration to cache frequently accessed FAQ data for optimized performance.
- **WYSIWYG Editor Support**: Rich text editor support for managing FAQ content, including text, images, and links.
- **Flexible Data Model**: Well-structured Django models for FAQ storage, with support for multilingual content.

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Caching**: Redis
- **Database**: PostgreSQL
- **Containerization**: Docker
- **WYSIWYG Editor**: `django-ckeditor`

## Installation

### Prerequisites

Before setting up the project, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/)
- [Docker](https://www.docker.com/) for containerized deployment (optional but recommended)
- [Redis](https://redis.io/) for caching (optional)

### Backend Setup

1. **Clone the Repository**  
   Clone the repository to your local machine:
    ```bash
    git clone https://github.com/anurag8773/FAQ-Backend.git
    cd FAQ-Backend
    ```

2. **Set Up a Virtual Environment**  
   It’s recommended to create a virtual environment to manage project dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**  
   Install the required Python dependencies listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**  
   The API uses PostgreSQL as the database. Ensure you have PostgreSQL installed and running, or configure it with Docker.  
   Run the following command to apply migrations:
    ```bash
    python manage.py migrate
    ```

5. **Set Up Redis (Optional)**  
   If you're using Redis for caching, install and start Redis on your machine or use Docker:
    ```bash
    docker run --name some-redis -p 6379:6379 -d redis
    ```

6. **Start the Django Development Server**  
   Run the Django development server:
    ```bash
    python manage.py runserver
    ```
   Your backend will be available at `http://localhost:8000`.

## File Structure

The project is structured as follows:

faq_project/
│── faq_project/          # Main Django project directory
│   │── __init__.py 
│   │── asgi.py           
│   │── settings.py       # Django settings file
│   │── urls.py           # Root URL configurations
│   │── wsgi.py           
│
│── faq/                  # Django app for FAQs
│   │── tests             # Unit tests for the app      
│   │── admin.py          # Django admin panel configurations
│   │── models.py         # Database models
│   │── serializers.py    
│   │── urls.py           # App-level URL routing
│   │── views.py          # API views (business logic)
│ 
│── Dockerfile
│── docker-compose.yml
│── manage.py             # Django CLI management script
│── README.md             # Project documentation
│── requirements.txt      # Dependencies for the project


- **backend/**: Contains the main Django project folder and app for FAQs.
- **faq_project/**: Project folder with Django settings, URL routing, and other configurations.
- **faqs/**: App containing models, views, serializers, and migrations related to FAQ data.
- **docker-compose.yml**: Configuration file for Docker containerization.
- **Dockerfile**: File for building the Docker image.
- **requirements.txt**: Python dependencies required for the project.

## API Usage Examples

### 1️⃣ Get All FAQs (Default: English)
- **Method**: GET  
- **URL**: `http://localhost:8000/api/faqs/`  
- **Description**: Fetch all FAQs in English by default.
  
**Response Example**:
```json
[
    {
        "id": 1,
        "question": "How does the FAQ API work?",
        "answer": "The FAQ API allows users to manage FAQs in different languages.",
        "lang": "en"
    },
    {
        "id": 2,
        "question": "How can I update an FAQ?",
        "answer": "Use the PUT request to update an FAQ.",
        "lang": "en"
    }
]
```

### 2️⃣ Get FAQs in Hindi
- **Method**: GET  
- **URL**: `http://localhost:8000/api/faqs/?lang=hi`  
- **Description**: Fetch FAQs in Hindi..
  
**Response Example**:
```json
[
    {
        "id": 1,
        "question": "FAQ API कैसे काम करता है?",
        "answer": "FAQ API उपयोगकर्ताओं को विभिन्न भाषाओं में FAQs को प्रबंधित करने की अनुमति देता है।",
        "lang": "hi"
    }
]
```

### 3️⃣ Create a New FAQ
- **Method**: POST  
- **URL**: `http://localhost:8000/api/faqs/`  
  
**Body**:
```json
[
    {
    "question": "What is a FAQ API?",
    "answer": "FAQ API helps users manage frequently asked questions.",
    "lang": "en"
  }
]
```

**Response Example**:
```json
[
    {
    "id": 3,
    "question": "What is a FAQ API?",
    "answer": "FAQ API helps users manage frequently asked questions.",
    "lang": "en"
    }
]
```


