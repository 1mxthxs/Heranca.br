# Generated by Django 3.2 on 2023-09-06 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0004_quizrelated'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_related',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizes.quizrelated'),
            preserve_default=False,
        ),
    ]
