# Generated by Django 4.1.3 on 2022-12-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="post", verbose_name="картинка"
            ),
        ),
    ]