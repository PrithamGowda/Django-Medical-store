from django.db import models

# Create your models here.
class Medicine(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=50,decimal_places=2)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.name
