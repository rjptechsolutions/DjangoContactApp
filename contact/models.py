from django.db import models
from datetime import datetime
class contact(models.Model):
  subject = models.CharField(max_length=50)
  Name = models.CharField(max_length=50)
  Email = models.CharField(max_length=50)
  Phoneno = models.CharField(max_length=12)
  Message = models.TextField()
  contact_at = models.DateTimeField(default=datetime.now, blank=True)  
  
  def __str__(self):
    return self.Name


  