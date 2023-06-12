from django.db import models

# Create your models here.
class New(models.Model):
    sl_no=models.IntegerField()
    item_name=models.CharField(max_length=150)
    description=models.CharField(max_length=200)


    def __str__(self):
        return self.item_name