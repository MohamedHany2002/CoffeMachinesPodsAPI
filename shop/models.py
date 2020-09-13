from django.db import models

# Create your models here.

MACHINE_TYPES =(('CML','COFFEE_MACHINE_LARGE'),('CMS','COFFEE_MACHINE_SMALL'),('EM','ESPRESSO_MACHINE'))
POD_TYPES = (('CPL','COFFEE_POD_LARGE'),('CPM','COFFEE_POD_SMALL'),('EP','ESPRESSO_POD'))

FLAVOUR_TYPES = (('CFV','COFFEE_FLAVOR_VANILLA'),('CFC','COFFEE_FLAVOR_CARAMEL'),('CFP','COFFEE_FLAVOR_PSL'),
                    ('CFM','COFFEE_FLAVOR_MOCHA'),('CFH','COFFEE_FLAVOR_HAZELNUT'))
PACK_SIZES = (('1dozen','1 dozen (12)'),('3dozen','3 dozen (36)'),
                ('5dozen','5 dozen (60)'),('7dozen','7 dozen (84)'))

class CoffeeMachine(models.Model):
    product_type = models.CharField(max_length=100,choices=MACHINE_TYPES)
    water_line = models.BooleanField(default=False)
    SKU = models.CharField(max_length=150)

    def __str__(self):
        return self.SKU

class CoffePod(models.Model):
    product_type = models.CharField(max_length=100,choices=POD_TYPES)
    coffee_flavor = models.CharField(max_length=100,choices=FLAVOUR_TYPES)
    pack_size = models.CharField(max_length=100,choices=PACK_SIZES)
    SKU = models.CharField(max_length=150)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.SKU