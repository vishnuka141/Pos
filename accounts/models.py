from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self,email,password,first_name,last_name,**extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("password is not provided")

        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,first_name,last_name,**extra_fields)

    def create_superuser(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

class User(AbstractUser,PermissionsMixin):

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    is_admin= models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    is_superadmin = models.BooleanField('Is superadmin', default=False)
    # options = (
    #     ("is_user", "is_user"),
    #     ("is_admin", "is_admin"),
    #     ("is_superadmin", "is_superadmin")
    # )
    # users=models.CharField(max_length=13,choices=options,default='is_user')



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
