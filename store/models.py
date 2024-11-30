from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the customer")
    email = models.EmailField(unique=True, help_text="Email address of the customer")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders",
        help_text="The customer who placed the order"
    )
    product = models.CharField(max_length=100, help_text="Name of the product ordered")
    quantity = models.PositiveIntegerField(help_text="Quantity of the product ordered")
    order_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the order was placed")
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total amount of the order"
    )

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
