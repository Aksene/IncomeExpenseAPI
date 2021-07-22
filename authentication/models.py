from django.db import models

# Create your models here.
# Import different needed authentication classes
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager,PermissionsMixin)

from django.db import models
from django.db.models.aggregates import Max


# Maintains which  query sets we can run
class UserManager(BaseUserManager):
    #Override the create user method
    def create_user(self, username, email, password=None):
        # Check for errors
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        
        # Define how user should be created
        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save
    
    # Override the SUPER create user method    
    def create_superuser(self, username, email, password=None):
        #Check for errors
        if password is None:
            raise TypeError('Passwrod should not be empty')
        
        # Create, save then return the requested user
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

# User model class
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255, unique=True, db_index= True)
    email=models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Now we login using email
    USERNAME_FIELD = 'email'
    # Determine which fields are required
    REQUIRED_FIELDS=['username']

    # Instantiate the UserManager class
    objects= UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''