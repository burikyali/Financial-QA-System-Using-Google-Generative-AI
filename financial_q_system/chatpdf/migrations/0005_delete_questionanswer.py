# Generated by Django 4.2.16 on 2024-12-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chatpdf", "0004_questionanswer"),
    ]

    operations = [
        migrations.DeleteModel(
            name="QuestionAnswer",
        ),
    ]
