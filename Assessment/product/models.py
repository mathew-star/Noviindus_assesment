from django.db import models
from django.conf import settings

class Product(models.Model):
    """
    Model to represent products available in the store.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    """
    Model to represent items in the user's cart.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    def get_total_price(self):
        return self.product.price * self.quantity
    
 