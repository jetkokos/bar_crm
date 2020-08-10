from django import forms
from .models import *
from django.utils.timezone import now


class CreateReportForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=now(), label="Дата")
    class Meta:
        model = Report
        labels = {
            'date': 'Дата',
            'cash_amount': 'Наличные',
            'card_amount': 'Терминал',
            'cashbox_morning': 'Касса утром',
            'cashbox_evening': 'Касса вечером',
            'cashbox_cash_added': 'Внесено в кассу',            
            'expense_cash': 'Расходы',
            'reason': 'На что потрачено',
        }
        exclude = ['created_by']

class UpdateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        labels = {
            'date': 'Дата',
            'cash_amount': 'Наличные',
            'card_amount': 'Терминал',
            'cashbox_morning': 'Касса утром',
            'cashbox_evening': 'Касса вечером',
            'cashbox_cash_added': 'Внесено в кассу',            
            'expense_cash': 'Расходы',
            'reason': 'На что потрачено',
        }
        exclude = ['date',  'created_by']



