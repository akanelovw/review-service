import uuid
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser


def get_confirmation_code(data):
    email = data.get('email')
    username = data.get('username')
    code = CustomUser.objects.update(
        confirmation_code=uuid.uuid4().hex.upper()
    )
    send_mail(
        'Confirmation',
        f'Your confirmation code {code}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
    return {'username': str(username), 'email': str(email)}
