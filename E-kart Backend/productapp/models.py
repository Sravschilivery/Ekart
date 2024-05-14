from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=(
            (1,'Mobile'),
            (2,'Shoes'),
            (3,'Clothes')
    )

    name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.FloatField(verbose_name="Price Per Item")
    qty=models.IntegerField(verbose_name="Quantity")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_available=models.BooleanField(verbose_name="Is_available")
    pdetails=models.CharField(max_length=100,verbose_name="Product Details")
    pimage=models.ImageField(upload_to='appimage/product',verbose_name="Upload Product Image")

    def __str__(self):
        return str(self.name)
