# Generated by Django 3.2 on 2023-09-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0005_quiz_quiz_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
