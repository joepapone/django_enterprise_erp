# Generated by Django 5.0.1 on 2024-01-22 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0003_delete_financialstatementlinesequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialStatementLineSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('financial_statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financials.financialstatement')),
                ('financial_statement_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financials.financialstatementline')),
            ],
        ),
    ]