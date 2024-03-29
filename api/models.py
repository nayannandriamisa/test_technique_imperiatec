from django.db import models

# Create your models here.
class Tache(models.Model):
    intitule = models.CharField(max_length=250)
    description = models.TextField(default=intitule)
    complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.intitule