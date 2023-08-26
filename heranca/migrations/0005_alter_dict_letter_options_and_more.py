# Generated by Django 4.2.4 on 2023-08-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("heranca", "0004_dict_letter_letter_char"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dict_letter",
            options={"ordering": ["alphabetical_order"]},
        ),
        migrations.AddField(
            model_name="dict_letter",
            name="alphabetical_order",
            field=models.IntegerField(default=0),
        ),
    ]