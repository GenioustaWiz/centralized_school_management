#accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.contrib.auth import get_user_model
from allauth.socialaccount.signals import pre_social_login,social_account_added, social_account_updated
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.core.files import File
from urllib.request import urlopen
from io import BytesIO

from PIL import Image 
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, request=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)


        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        # Resize the image
        img = Image.open(user.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(user.image.path)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    USER_TYPES = (
        ('master_admin', 'Master Admin'),
        ('lead_admin', 'Lead Admin'),
        ('data_admin', 'Data Admin'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
        ('government_official', 'Government Official'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Specify a related name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Specify a related name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    objects = UserManager()
    
    def __str__(self):
        return f'{self.email} User' #show how we want it to be displayed


# this acts asa signal for updating entries on the user  model from data gotten from social login
@receiver(pre_social_login, dispatch_uid='pre_social_login_signal')
@receiver(social_account_updated, dispatch_uid='social_account_updated_signal')
def populate_user_profile(sender, request, sociallogin, **kwargs):
    if sociallogin:
        # Extract the email from the social account data
        social_email = sociallogin.account.extra_data.get('email', None)
        if social_email:
            # Check if a user with this email already exists
            existing_user = User.objects.filter(email=social_email).first()
            # User with this email doesn't exists, handle accordingly
            if not existing_user:
                sociallogin.save(request)
                
    user_model = get_user_model()
    user_data = sociallogin.account.extra_data
    email = user_data['email']

    # Additional logic based on social account provider
    # if sociallogin.account.provider == 'facebook':

    if sociallogin.account.provider == 'google':
        image_url = user_data['picture']
        image_content = urlopen(image_url).read()
        image_file = BytesIO(image_content)
        sociallogin.account.user.image.save('profile.jpg', File(image_file))
        # Split full name into first and last names
        full_name = user_data.get('name', '')
        if full_name:
            names = full_name.split()
            sociallogin.account.user.first_name = names[0] if names else ''
            sociallogin.account.user.last_name = ' '.join(names[1:]) if len(names) > 1 else ''
        else:
            sociallogin.account.user.first_name = ''
    
    
    # Save the user object    
    sociallogin.account.user.save()

    # Resize the image
    img = Image.open(sociallogin.account.user.image.path)
    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(sociallogin.account.user.image.path)