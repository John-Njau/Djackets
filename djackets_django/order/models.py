from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    email = models.EmailField(),
    address = models.CharField(max_length=250),
    zipcode = models.CharField(max_length=20),
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)
    # updated = models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        self.first_name
        
class OrderItem(models.Model):
    # referencing the order
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # referencing the product
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    
    # string representation
    def __str__(self):
        return '%s' % (self.id)
