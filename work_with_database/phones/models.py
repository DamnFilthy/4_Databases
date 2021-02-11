from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.TextField(max_length=300)
    release_date = models.TextField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(default='mobile')




