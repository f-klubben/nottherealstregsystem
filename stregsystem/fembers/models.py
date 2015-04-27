from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=64, null=True, blank=True)
    name = models.CharField(max_length=64, default='')
    number = models.IntegerField()
    join_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    _pin = models.CharField(verbose_name="pin",
                            max_length=128,
                            blank=True,
                            null=True)
    note = models.TextField(blank=True)
    email = models.EmailField()
    _phone_number = models.CharField(verbose_name="phone number",
                                     max_length=16,
                                     blank=True,
                                     validators=[])

    def __str__(self):
        return str.format("{s.username} #{s.number} ({s.name})", s=self)


class List(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name
