import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import CustomUser

OUR_DATABASE = {
    CustomUser: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):
    help = 'Загружает базы данных из CSV файлов'

    def handle(self, *args, **options):
        for model, base in OUR_DATABASE.items():
            path = f'{settings.BASE_DIR}/static/data/{base}'
            with open(path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(model(**data) for data in reader)
            self.stdout.write(
                self.style.SUCCESS(f'Модель {model.__name__} загружена')
            )
