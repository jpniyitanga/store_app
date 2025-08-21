from django.db import models


class Promotion(models.Model):
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.description


class Tag(models.Model):
    name = models.CharField(max_length=55, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=255)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    # products remain if category is deleted
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)
    promotions = models.ManyToManyField(Promotion, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# 2:12 mark
