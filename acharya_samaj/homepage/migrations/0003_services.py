# Generated by Django 4.0.4 on 2023-06-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_messageofbod_notices_programs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=2000)),
                ('images', models.ImageField(blank=True, upload_to='Services/images/')),
                ('videos', models.FileField(blank=True, upload_to='Services/video/')),
            ],
        ),
    ]
