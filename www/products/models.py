from django.db import models



# Create your models here.


class CategoryProduct(models.Model):
    name = models.CharField(max_length=100)
    dsc = models.CharField(max_length=350)
    image = models.ImageField(upload_to='ProductCategoryImage',blank=True,null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=112)
    dsc = models.CharField(max_length=550)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=3400)
    category = models.ForeignKey(to=CategoryProduct,on_delete=models.CASCADE)
    

    click_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return F"{self.name} | {self.price}   ----|\__( click:{self.click_count})"





