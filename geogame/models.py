from django.db import models

# Create your models here.

class Amodel(models.Model):
    """
    This is a model just to test auto migrations on Heroku deploy.
    """
    name = models.CharField('Name', max_length=100)
