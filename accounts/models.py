from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='doctor')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
