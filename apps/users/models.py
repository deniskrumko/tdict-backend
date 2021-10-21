from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Model for app user."""

    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='Email',
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('email',)

    @property
    def full_name(self):
        """Get full name of user."""
        return f'{self.first_name} {self.last_name}'
