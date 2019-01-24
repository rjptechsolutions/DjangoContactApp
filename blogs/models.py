from django.db import models
from datetime import datetime

class BlogModel(models.Model):
  title = models.CharField(max_length=70)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  is_published = models.BooleanField(default=True)
  author = models.CharField(max_length=50)

  def __str__(self):
    return self.title
  