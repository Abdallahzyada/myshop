from django.db import models
from shop.models import Product

# Create your models here.
class Order (models.Model):
   first_name=models.CharField( max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   address = models.CharField(max_length=250)
   postal_code = models.CharField(max_length=20)
   city = models.CharField(max_length=100)
   created = models.DateTimeField(auto_now=False, auto_now_add=True)
   updated = models.DateTimeField(auto_now=True, auto_now_add=False)
   paid = models.BooleanField(default=False)

   #Metadata
   class Meta :
       ordering = ['-created']
       indexes = [models.Index(fields=['-created']),]


   #Methods
   def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

   def __str__(self):
        return f'Order {self.id}'
   

class OrderItem (models.Model):
   order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
   product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.PositiveIntegerField(default=1)

   #Methods

   def __str__(self):
       return str(self.id)
   def get_cost(self):
       return self.price * self.quantity