from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import Account


class LikedItem(models.Model):
    # What tag is applied to what object
    # customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    # Generic relationship to be able to tag any type of object. Ex: Product, Brand
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    # def __str__(self):
    #     return f"{self.customer} liked {self.content_object}"
