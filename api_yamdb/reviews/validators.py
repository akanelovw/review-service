from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > datetime.now().year:
        raise ValidationError('Будущее непредсказуемо')


def validate_score(value):
    if value not in range(1, 10):
        raise ValidationError('Ожидается оценка от 1 до 10')
