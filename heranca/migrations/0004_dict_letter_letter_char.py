# Generated by Django 3.2 on 2023-08-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heranca', '0003_dict_indigenous_dict_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='dict_letter',
            name='letter_char',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
    ]
