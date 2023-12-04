from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=20000000)
    pub_date = models.DateTimeField("Date published")
    created_date = models.DateTimeField("Date created")

    def __str__(self) -> str:
        return self.title