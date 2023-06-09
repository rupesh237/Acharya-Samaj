# Generated by Django 4.0.4 on 2023-06-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JoinAcharya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('nationality_card', models.ImageField(upload_to='homepage/JoinAcharya/%d')),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='messageofbod',
            name='photo',
            field=models.ImageField(upload_to='MessageBOD/photo/'),
        ),
        migrations.AlterField(
            model_name='messageofbod',
            name='video',
            field=models.FileField(blank=True, upload_to='MessageBOD/video/'),
        ),
        migrations.AlterField(
            model_name='notices',
            name='images',
            field=models.ImageField(blank=True, upload_to='notices/images/'),
        ),
        migrations.AlterField(
            model_name='notices',
            name='video_file',
            field=models.FileField(blank=True, upload_to='notices/videos/%d'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='video_file',
            field=models.FileField(blank=True, upload_to='programs/video/%d'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='images',
            field=models.ImageField(upload_to='slider/images/%d'),
        ),
    ]
