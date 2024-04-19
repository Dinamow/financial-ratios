# Generated by Django 4.2.2 on 2024-04-18 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10, unique=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Ratios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_shares', models.FloatField(default=0.0, verbose_name='Number of Shares')),
                ('market_price', models.FloatField(default=0.0, verbose_name='Market Price')),
                ('net_income', models.FloatField(default=0.0, verbose_name='Net Income')),
                ('sales', models.FloatField(default=0.0, verbose_name='Sales')),
                ('total_assets', models.FloatField(default=0.0, verbose_name='Total Assets')),
                ('total_equity', models.FloatField(default=0.0, verbose_name='Total Equity')),
                ('ebit', models.FloatField(default=0.0, verbose_name='EBIT')),
                ('interest', models.FloatField(default=0.0, verbose_name='Interest Expense')),
                ('tax_rate', models.FloatField(default=0.0, verbose_name='Tax Rate')),
                ('dividends', models.FloatField(default=0.0, verbose_name='Dividends')),
                ('total_fixed_assets', models.FloatField(default=0.0, verbose_name='Fixed Assets')),
                ('total_current_assets', models.FloatField(default=0.0, verbose_name='Total Current Assets')),
                ('cogs', models.FloatField(default=0.0, verbose_name='Cost of Revenue, Total')),
                ('inventory', models.FloatField(default=0.0, verbose_name='Total Inventory')),
                ('account_receivables', models.FloatField(default=0.0, verbose_name='Total Receivables, Net')),
                ('account_payable', models.FloatField(default=0.0, verbose_name='Accounts Payable')),
                ('cash', models.FloatField(default=0.0, verbose_name='Cash & Equivalents')),
                ('total_current_liability', models.FloatField(default=0.0, verbose_name='Total Current Liabilities')),
                ('total_debt', models.FloatField(default=0.0, verbose_name='Total Debt')),
                ('ebitda', models.FloatField(default=0.0, verbose_name='EBITDA')),
                ('dividansRatio', models.FloatField(default=0.0, editable=False, verbose_name='Dividans Ratio')),
                ('book_value', models.FloatField(default=0.0, editable=False, verbose_name='Book Value')),
                ('eps', models.FloatField(default=0.0, editable=False, verbose_name='EPS')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dates')),
            ],
        ),
    ]
