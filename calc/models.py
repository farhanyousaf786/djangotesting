from django.db import models
from django.urls import reverse

# Create your models here.
        
class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    type = models.TextField()
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'snowglobe_id': self.id})