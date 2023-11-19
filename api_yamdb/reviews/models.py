from django.db import models

from users.models import CustomUser
from .validators import validate_score, validate_year


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=256)
    slug = models.SlugField(verbose_name='Слаг', unique=True, max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=256)
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название произведения',
        max_length=256)
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year])
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        blank=False, null=True)
    genre = models.ManyToManyField(
        Genre, related_name='titles',
        verbose_name='Жанр',
        blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        indexes = [models.Index(fields=['year']),
                   models.Index(fields=['name'])]


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Автор')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        null=True)
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=[validate_score])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='title_author_review'
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True)
