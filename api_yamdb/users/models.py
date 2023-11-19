from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
SUPER_USER = 'super_user'

ROLES = (
    (USER, 'user'),
    (MODERATOR, 'moderator'),
    (ADMIN, 'admin'),
    (SUPER_USER, 'super_user'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, blank=False,
                              null=False)
    role = models.CharField(max_length=15, choices=ROLES, default=USER)
    bio = models.TextField(blank=True)
    confirmation_code = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return ({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR
