# Generated by Django 4.0.1 on 2022-06-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='place_image',
            field=models.CharField(max_length=200),
        ),
    ]