# Generated by Django 3.2 on 2023-06-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ConfirmationCode',
        ),
    ]