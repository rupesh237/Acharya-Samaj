from django.db import models

# Create your models here.

class Slider(models.Model):
    title= models.CharField(max_length=60, blank=True)
    description= models.CharField(max_length=1000, blank=True)
    images= models.ImageField(upload_to='slider/images/%d', blank=False)

    def __str__(self):
        return self.title


class Programs(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description= models.CharField(blank=False, max_length=5000)
    images=models.ImageField(blank=True)
    video_file= models.FileField(upload_to='programs/video/%d', blank=True)

    def __str__(self):
        return f"{self.title} {self.images}"


class Notices(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description= models.CharField(blank=False, max_length=5000)
    images=models.ImageField(blank=True, upload_to='notices/images/')
    video_file= models.FileField(upload_to='notices/videos/%d', blank=True)

    def __str__(self):
        return self.title


class MessageOfBOD(models.Model):
    post= models.CharField(max_length=30, blank=False)
    name= models.CharField(max_length=50, blank=False)
    message= models.CharField(max_length=1500, blank=False)
    photo= models.ImageField(upload_to='MessageBOD/photo/', blank=False)
    video= models.FileField(upload_to='MessageBOD/video/', blank=True)

    def __str__(self):
        return f"{self.name} ({self.post})"


class Services(models.Model):
    title= models.CharField(max_length=60, blank=False)
    description= models.CharField(max_length=2000)
    images= models.ImageField(upload_to='Services/images/', blank=True)
    videos= models.FileField(upload_to='Services/video/', blank=True)


    def __str__(self):
        return self.title
    

class JoinAcharya(models.Model):
    name =models.CharField(max_length=50)
    address= models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    nationality_card = models.ImageField(upload_to="homepage/JoinAcharya/%d")
    message= models.TextField()

    def __str(self):
        return f"{self.name} {self.nationality_card}"


class ContactUsDB(models.Model):
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    message= models.TextField()


    def __str__(self):
        return f"{self.name} {self.message}"
