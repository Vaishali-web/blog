from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Entry(models.Model):
    entry_title=models.CharField(max_length=300)
    entry_text=models.TextField()
    entry_date=models.DateTimeField(auto_now_add=True)
    entry_author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="entries"
    def __str__(self):
        return (self.entry_title)

    def get_absolute_url(self):
        return reverse('blog-travel-detail',kwargs={"pk":self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pics is a folder to store uploaded pics
    image = models.ImageField(default='https://picsum.photos/200',upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    entry=models.ForeignKey(Entry,on_delete=models.CASCADE)
    entry_text=models.TextField()

    # function to resize image
    # overite existing image size with latest image


# Create your models here.
