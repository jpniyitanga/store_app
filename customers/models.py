from django.db import models


class Customer(models.Model):
    user = models.OneToOneField('accounts.Account', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True)
    default_address = models.ForeignKey(
        'customers.Address', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    def __str__(self):
        return self.user.email


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return f"{self.street}, {self.city}"
