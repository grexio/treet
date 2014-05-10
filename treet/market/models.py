from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Treet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)
    video = models.CharField(verbose_name="Youtube Video ID", max_length=20)

    def __str__(self):
        return self.title
