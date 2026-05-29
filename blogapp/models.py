from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.CharField(max_length=500, default="sd")
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def get_absolute_url(self):
        return reverse('displaypage')

    def __str__(self):
        return self.title


class readmore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    readmore = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='read_blog')


class Favblog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE
    )
