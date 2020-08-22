from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
class ExternalForm(models.Model):
      title = models.CharField(max_length=64, verbose_name="Источник")
      uid = models.CharField(max_length=32, default=get_random_string(length=32))
      
      def __str__(self):
        return self.title
      