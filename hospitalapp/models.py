from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class MyUserManager():
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password):
        user = self.create_user(
            username,
            password=password,
            name=name,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Register(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    gender_choice = (('Male', 'male'), ('Female', 'female'), ('Other', 'other'))
    gender = models.CharField(max_length=6, choices=gender_choice)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyUserManager()

    def __str__(self):
        return self.username

class Appointment(models.Model):
    username = models.CharField(max_length=20, default='avinash')
    patient_name = models.CharField(max_length=30)
    doctor_choice = (('Ms.Krishna', 'Ms.Krishna'), ('Ms.Bhavani', 'Ms.Bhavani'), ('Ms.Gireesha', 'Ms.Gireesha'))
    doctor_name = models.CharField(max_length=15, choices=doctor_choice)
    timings_choice = (('10:00 A.M - 11:00 A.M', '10:00 A.M - 11:00 A.M'), ('11:00 A.M - 12:00 P.M', '11:00 A.M - 12:00 P.M'), ('2:00 P.M - 3:00 P.M', '2:00 P.M - 3:00 P.M'), ('4:00 P.M - 5:00 P.M', '4:00 P.M - 5:00 P.M'), ('5:00 P.M - 6:00 P.M', '5:00 P.M - 6:00 P.M'))
    timings = models.CharField(max_length=30, choices=timings_choice)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    symptoms = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default='Pending')
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.patient_name

class ContactUs(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name