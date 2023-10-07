from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    img_url = models.URLField()

    DisplayFields = [
        "id",
        "title",
        "description",
        "link",
        "img_url",
    ]

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    hero_image = models.URLField()
    mini_about = models.TextField(blank=True)
    about = models.TextField()

    DisplayFields = [
        "id",
        "title",
        "subtitle",
        "hero_image",
        "mini_about",
        "about",
    ]

    def __str__(self):
        return self.title
