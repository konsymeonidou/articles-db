import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'articlesdb.settings')
django.setup()

from django.contrib.auth.models import User

def create_users():
    # Create two superusers
    User.objects.create_superuser(username='admin1', email='admin1@example.com', password='password1')

    # Create regular users
    User.objects.create_user(username='user2', email='user2@example.com', password='password2')

    print("Users created successfully.")

if __name__ == '__main__':
    create_users()