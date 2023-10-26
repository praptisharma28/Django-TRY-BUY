from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.CharField(max_length=1222)
    def __str__(self) -> str:
        return self.name
