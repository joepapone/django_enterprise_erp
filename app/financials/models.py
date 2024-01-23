from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class FinancialStatementType(models.Model):
    class Type(models.TextChoices):
        INCOME_STATEMENT = 'IS', _("Income Statement")
        BALANCE_SHEET = 'BS', _("Balance Sheet")
        CASH_FLOW_STATEMENT = 'CF', _("Cash Flow Statement")

    type = models.CharField(max_length=2, choices=Type)

    def __str__(self):
        return self.type


class FinancialStatement(models.Model):
    name = models.CharField(max_length=100, null=False)


class FinancialStatementLine(models.Model):
    tag = models.CharField(max_length=50, null=False, unique=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    

class FinancialStatementLineSequence(models.Model):
    sequence = models.IntegerField(null=False)
    financial_statement = models.ForeignKey(FinancialStatement, on_delete=models.CASCADE, null=False)
    financial_statement_line = models.ForeignKey(FinancialStatementLine, on_delete=models.CASCADE, null=False)

