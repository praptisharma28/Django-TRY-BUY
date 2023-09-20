from django.db import models

class Login(models.Model):
    Username=models.CharField( max_length=122)
    Password=models.CharField(max_length=122)
    def __str__(self) -> str:
        return self.Username
    
class Signup(models.Model):
    Username=models.CharField( max_length=122)
    Password=models.CharField(max_length=122)
    Confirm_Password=models.CharField(max_length=122)
    def __str__(self) -> str:
        return self.Username
