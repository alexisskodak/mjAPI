from django.db import models


class Contact(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName


class Retailer(models.Model):
    shopName = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to='pictures/retailers/')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField()
    available = models.BooleanField()
    SIRET = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.shopName} - {self.contact.firstName}'

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'


class DeliveryPartner(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/delivery-staff/')
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField()

    def __str__(self):
        return f'Delivery partner - {self.contact.firstName}'


class Customer(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField()
    favoriteShops = models.ManyToManyField(Retailer)

    def __str__(self):
        return f'Customer - {self.contact.firstName}'


class Category(models.Model):
    label = models.CharField(max_length=100)
    glyph = models.ImageField(upload_to='glyphs/')

    def __str__(self):
        return self.label


class Images(models.Model):
    image = models.ImageField(upload_to='products/')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pricingModel = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    retailer = models.ForeignKey(Retailer, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(blank=True, null=True)
    prepTime = models.IntegerField()

    def __str__(self):
        return f'Type: {self.category.label}, Name: {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    retailer = models.ForeignKey(Retailer, on_delete=models.DO_NOTHING)
    deliveryPartner = models.ForeignKey(DeliveryPartner, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100)
    shippedAt = models.DateTimeField()
    deliveredAt = models.DateTimeField()

    def __str__(self):
        return f'Order n {self.id}'
