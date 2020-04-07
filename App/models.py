from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from django.utils import timezone


class Agreement(models.Model):
   agreement_name = models.CharField(max_length=100, verbose_name="Discount Agreement")
   company = models.CharField(max_length=100, verbose_name="Company")
   country = models.CharField(max_length=100, verbose_name="Country")
   user_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Responsible person"
    )

   class Meta:
       verbose_name = "Agreement"
       verbose_name_plural = "agreements"

   def __str__(self):
       return "{} - {} - {}".format(self.agreement_name.title(), self.company.title(), self.country.title())


class Periods(models.Model):
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        verbose_name="Discount Agreement"
    )

    period_start = models.DateField(default=timezone.now(), verbose_name="Start period of agreement")
    period_finish = models.DateField(default=datetime.now() + timedelta(days=31), verbose_name="Finish period of agreement")

    class Meta:
        verbose_name = "periods"
        verbose_name_plural = "periods"

    def __str__(self):
        return "{}: {} - {}".format(self.agreement.agreement_name.title(), self.period_start.strftime("%d.%m.%Y"), self.period_finish.strftime("%d.%m.%Y"))
