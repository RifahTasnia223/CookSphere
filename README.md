# CookSphere

CookSphere is a Facebook-like social media platform for cooking enthusiasts, built with Django. Users can share recipes as posts, upload images, like and comment on recipes, and manage their own profiles with profile pictures. The site features a modern, responsive Bootstrap 5 UI.

## Features

- Central feed of all user recipe posts
- Persistent likes and comments on recipes
- User registration, login, and authentication (with allauth)
- User profiles with profile pictures and editable bio, location, and birth date
- Image uploads for both recipes and user profiles (stored locally)
- View any user's public profile and their profile picture
- Only the author can delete their own posts
- Responsive, mobile-friendly Bootstrap 5 theming throughout

## Getting Started

### Prerequisites
- Python 3.9+
- Django 4.2+
- (Recommended) Virtual environment

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd CookSphere.-master
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Usage
- Visit `http://127.0.0.1:8000/social/` for the main feed
- Register or log in to post, like, or comment
- Click on any username or profile picture to view a user's profile
- Edit your profile and upload a profile picture from the Profile page
- Create, view, and delete your own recipe posts

### Media & Static Files
- Uploaded images are stored locally in the `media/` directory
- Static files (Bootstrap, CSS) are managed via Django's staticfiles

### Customization
- Allauth is used for authentication; templates are Bootstrap-themed
- No group features—focus is on individual users and recipes

## License
MIT License

---
CookSphere is a project for learning and sharing recipes in a social, interactive way. Enjoy cooking and connecting!