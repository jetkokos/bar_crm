from django.db import models
from django.contrib.auth.models import User
# from datetime import date

# Create your models here.

class Report(models.Model):
    date = models.DateField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    cash_amount = models.FloatField()
    card_amount = models.FloatField()
    cashbox_morning = models.FloatField()
    cashbox_evening = models.FloatField()
    cashbox_cash_added = models.FloatField(default=0)
    expense_cash = models.FloatField(blank=True,default=0)
    reason = models.CharField(max_length=300, blank=True)

    def cashbox_difference(self):
        return (self.cashbox_evening - (self.cashbox_morning + self.cash_amount - self.expense_cash + self.cashbox_cash_added))

    def summ_cash_and_card_proceed(self):
        return (self.cash_amount + self.card_amount)

    # def today_check(self):
    #     return date.today() == self.date

    def __str__(self):
        return str(self.date) + ' ' + str(self.created_by) 






