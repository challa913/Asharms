from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    Group, Permission, PermissionsMixin)
from ashrams.models.base import Base


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, address, phone, password=None, email=None):
        """
        Creates and saves a Myuser with the given email, date of
        birth and password.
        """

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, phone, first_name, last_name, email=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('User must have an user name')
        if not first_name:
            raise ValueError('User must have an first name')
        if not last_name:
            raise ValueError('User must have an last name')
        if not phone:
            raise ValueError('User must have a phone number')


        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_admin=True,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin, Base):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(
        verbose_name='email',
        max_length=255, null=True, blank=True
    )
    address = models.TextField(blank=True, null=True)
    phone = models.IntegerField(max_length=10)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __init__(self, *args, **kwargs):
        self._meta.get_field_by_name('groups')[0].blank = False
        super(MyUser, self).__init__(*args, **kwargs)

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        app_label = 'myuser'