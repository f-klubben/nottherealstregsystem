from django.db import models
from django.utils import html


class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PointOfSale(models.Model):
    name = models.CharField(max_length=64)
    listings = models.ManyToManyField('Listing')

    def __str__(self):
        return self.name


class Listing(models.Model):
    _name = models.CharField(verbose_name="name",
                             max_length=64,
                             null=True,
                             blank=True)
    number = models.IntegerField()
    price = models.IntegerField()
    product = models.ForeignKey('Product')

    @property
    def name(self):
        if self._name:
            return self._name
        else:
            return self.product.name

    @name.setter
    def name(self, n):
        self._name = n

    def __str__(self):
        name = html.strip_tags(self.name)
        return str.format("{name} #{s.number} ({s.price})", name=name, s=self)


class Tag(models.Model):
    name = models.CharField(max_length=64)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        # should ensure that we get no tag dupes
        unique_together = ("name", "value")
