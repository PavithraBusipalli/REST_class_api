from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    PrdctCat_id = models.IntegerField(primary_key = True)
    PrdctCat_name = models.CharField(max_length = 10)

    def __str__(self):
        return self.PrdctCat_name

class Product(models.Model):
    PrdctCat_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    Prdct_name = models.CharField(max_length=10)
    Prdct_id = models.IntegerField()
    Prdct_price = models.IntegerField()
    Prdct_brand = models.CharField(max_length = 10)

    def __str__(self):
        return self.Prdct_name
    