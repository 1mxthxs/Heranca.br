# Generated by Django 3.2 on 2023-09-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0008_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='required_score_to_pass',
            field=models.IntegerField(help_text='required score, Ex: 6, then (6=score/10=questions) to pass'),
        ),
    ]
