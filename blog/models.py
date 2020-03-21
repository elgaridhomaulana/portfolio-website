from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title
