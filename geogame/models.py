from django.db import models

# Create your models here.


class Scenario(models.Model):
    """
    Game scenario as a sequence of steps
    """
    name = models.CharField('Name', max_length=200)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.name


class Amodel(models.Model):
    """
    This is a model just to test auto migrations on Heroku deploy.
    """
    name = models.CharField('Name', max_length=100)
