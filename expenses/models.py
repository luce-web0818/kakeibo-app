from django.db import models

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.date}{self.category}{self.amount}"

# Create your models here.
