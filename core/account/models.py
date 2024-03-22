from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group , Permission

class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is Required')
        user = self.model(email=self.normalize_email(username), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    # Specify a custom related_name for the groups field
    groups = models.ManyToManyField(Group, related_name='user_data_groups')
    # Define a related_name to differentiate from auth.User's user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='user_permissions_custom'
    )

    def __str__(self):
        return self.first_name

