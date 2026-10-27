from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES=[
        ('Cleanser','Cleanser'),
        ('Moisturizer','Moisturizer'),
        ('Sunscreen','Sunscreen'),
        ('Other','Other'),
    ]
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}({self.category})"