from django.db import models


class Product(models.Model):
    x = [
    ('phone', 'phone'),
    ('laptop', 'laptop')
]

    name = models.CharField(max_length=50 )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d' ,blank=True)
    active = models.BooleanField(default=True)
    category=models.CharField(max_length=50 ,null=True ,blank=True ,choices=x , default='select')


    
    def __str__(self):
        return self.name  
