from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Retailer(models.Model):
    shop_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to='pictures/retailers/')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField(default=69001)
    available = models.BooleanField()
    SIRET = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.shop_name} - {self.contact.first_name}'

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'


class DeliveryPartner(models.Model):
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/delivery-staff/')
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField(default=69001)

    def __str__(self):
        return f'Delivery partner - {self.contact.first_name}'

    class Meta:
        verbose_name = 'Delivery Partner'
        verbose_name_plural = 'Delivery Partners'


class Images(models.Model):
    image = models.ImageField(upload_to='products/')


class Category(models.Model):
    label = models.CharField(max_length=100)
    glyph = models.ImageField(upload_to='glyphs/', default='')

    def __str__(self):
        return self.label


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pricing_model = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField()

    def __str__(self):
        return f'Type: {self.category.label}, Name: {self.name}'


class Customer(models.Model):
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=25)
    zip = models.IntegerField(default=69001)
    favorite_shops = models.ManyToManyField(Retailer)
    favorite_products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Customer - {self.contact.first_name}'


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
