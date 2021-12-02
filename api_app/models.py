from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager) :
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
       
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_active=True,
                          last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, 
                                 **extra_fields)
        
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self, filename):
    return f'profile_image/{str(self.pk)}/{"profile_image.png"}'

def get_default_profile_image():
    return 'bizkonect/logo_1080_1080.png'

class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, upload_to=get_profile_image_filepath,blank=True,default=get_default_profile_image)
    country = models.CharField(max_length=100, blank=True, null=True)    
    description = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    certification = models.CharField(max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','country','language',]
    
    def _str_(self) :
        return self.email

    def get_profile_image_filename(self) :
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label) :
        return True

