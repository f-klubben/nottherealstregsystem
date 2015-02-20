from django.db import models

from catalog.models import Product
from fembers.models import Member


class Transaction(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=64, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    member = models.ForeignKey(Member, null=True, blank=True)

    def __str__(self):
        if self.is_payment():
            result = str.format("{m.username} <- ({s.value})",
                                m=self.member,
                                s=self)
        elif self.is_sale():
            result = str.format("{m.username} -> {p.name} ({s.value})",
                                p=self.product,
                                m=self.member,
                                s=self)
        else:
            result = str.format("{s.name} ({s.value})", s=self)

        return result

    def is_payment(self):
        return self.value > 0

    def is_sale(self):
        return self.value < 0
