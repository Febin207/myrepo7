from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Categorys')

    def __str__(self):
        return self.name
class Product(models.Model):
    #product_id = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Products')
    available = models.BooleanField(default=False)
    stock = models.IntegerField()

    def __str__(self):
        return self.name