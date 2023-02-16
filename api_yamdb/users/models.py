from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        choices=settings.USER_ROLE_CHOICES,
        default='user',
        max_length=15,
    )
    confirmation_code = models.CharField(
        'код подтверждения',
        max_length=255,
        null=True,
        blank=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'), name='username_email_unique'
            )
        ]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == settings.ADMIN

    @property
    def is_moderator(self):
        return self.role == settings.MODERATOR

    @property
    def is_user(self):
        return self.role == settings.USER
