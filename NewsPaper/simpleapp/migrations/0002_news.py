# Generated by Django 5.0.3 on 2024-05-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_News', models.CharField(max_length=50, unique=True)),
                ('text_News', models.TextField()),
            ],
        ),
    ]
