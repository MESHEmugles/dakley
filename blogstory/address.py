from django.db import models

class Address(models.Model):

    ip = models.CharField(max_length=40, unique=True, default = '0.0.0.0', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.ip



