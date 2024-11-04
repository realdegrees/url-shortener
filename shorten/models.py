from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField()
    code = models.CharField(max_length=50)
    # TODO add foreign user id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)