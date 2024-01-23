from django.db import models

# Create your models here.



# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)


    def __str__(self):
        return self.name
