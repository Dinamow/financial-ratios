from django.test import TestCase
from .models import *
import random

def get_values(company, date):
    return {"number_of_shares": 1000000,
            "market_price": 50.25,
            "net_income": 5000000,
            "sales": 20000000,
            "total_assets": 30000000,
            "total_equity": 15000000,
            "ebit": 8000000,
            "interest": 1000000,
            "tax_rate": 0.25,
            "dividends": 2000000,
            "total_fixed_assets": 10000000,
            "total_current_assets": 20000000,
            "cogs": 10000000,
            "inventory": 5000000,
            "account_receivables": 7000000,
            "account_payable": 4000000,
            "cash": 3000000,
            "total_current_liability": 6000000,
            "total_debt": 8000000,
            "ebitda": 9000000,
            "company": company,
            "date": date}

# Create your tests here.
class MyTests(TestCase):
    
    def setUp(self):
        self.engine = Engine()
        company = Company.objects.create(name="DINAMOW")
        date = Dates.objects.create(date='2023')
        Ratios.objects.create(**get_values(company, date))
        self.engine.date(company="DINAMOW",year='2023')

    def test_testing(self):
        """test the testing view"""
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'foo': 'bar'})
    
    def test_dates(self):
        """test the dates view"""
        response = self.client.get('/api/v1/dates/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"dates": self.engine.get_dates()})
    
    def test_get_current_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_current_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_cash_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_cash_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_debt_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_debt_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_debt_equity_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_debt_equity_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_equity_multiplier_value(self):
        """test the balance view"""
        ca = self.engine.get_equity_multiplier_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_times_interest_earned_value(self):
        """test the balance view"""
        ca = self.engine.get_times_interest_earned_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_ebitda_coverage_value(self):
        """test the balance view"""
        ca = self.engine.get_ebitda_coverage_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_total_assets_turnover_value(self):
        """test the balance view"""
        ca = self.engine.get_total_assets_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_current_assets_turnover_value(self):
        """test the balance view"""
        ca = self.engine.get_current_assets_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_inventory_turnover_value(self):
        """test the balance view"""
        ca = self.engine.get_inventory_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_days_sales_in_inventory_value(self):
        """test the balance view"""
        ca = self.engine.get_days_sales_in_inventory_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_receivables_turnover_value(self):
        """test the balance view"""
        ca = self.engine.get_receivables_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_days_sales_in_receivables_value(self):
        """test the balance view"""
        ca = self.engine.get_days_sales_in_receivables_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_payables_turnover_value(self):
        """test the balance view"""
        ca = self.engine.get_payables_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_net_profit_margin_value(self):
        """test the balance view"""
        ca = self.engine.get_net_profit_margin_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_return_on_assets_value(self):
        """test the balance view"""
        ca = self.engine.get_return_on_assets_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_return_on_equity_value(self):
        """test the balance view"""
        ca = self.engine.get_return_on_equity_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_return_on_investment_value(self):
        """test the balance view"""
        ca = self.engine.get_return_on_investment_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_return_trade_on_equity_value(self):
        """test the balance view"""
        ca = self.engine.get_return_trade_on_equity_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_return_trade_on_equity_using_EVA_value(self):
        """test the balance view"""
        ca = self.engine.get_return_trade_on_equity_using_EVA_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_internal_growth_rate_value(self):
        """test the balance view"""
        ca = self.engine.get_internal_growth_rate_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_eps_value(self):
        """test the balance view"""
        ca = self.engine.get_eps_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_pe_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_pe_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_mb_ratio_value(self):
        """test the balance view"""
        ca = self.engine.get_mb_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_fair_value_of_stock_value(self):
        """test the balance view"""
        ca = self.engine.get_fair_value_of_stock_value()
        self.assertNotEqual(ca, 0.0)

    # def test_get_ratio(self):
    #     """test the balance view"""
    #     years = ['2023']
    #     ratio = 'Current Ratio'
    #     company = 'DINAMOW'
    #     sample = self.engine.get_ratio(ratio, years, company)
    #     # print(sample)

    def test_get_type(self):
        """test the balance view"""
        years = ['2023', '2022'] # Needs to be tested with multiple years
        type = 'Liquidity'
        sample = self.engine.get_type(type, years, company='DINAMOW')
        print(sample)

    # def test_get_ratio(self):
    #     """test the balance view"""
    #     years = ['2023']
    #     ratio = 'Current Ratio'
    #     sample = self.engine.get_ratio(ratio, years, company='DINAMOW')
    #     # print(sample)

    # def test_get_ratios(self):
    #     """test the balance view"""
    #     years = ['2023']
    #     ratios = ['Current Ratio', 'Cash Ratio']
    #     sample = self.engine.get_ratios(ratios, years, company='DINAMOW')
    #     # print(sample)

    # def test_get_statements(self):
    #     """test the balance view"""
    #     years = ['2023']
    #     statements = ['Balance Sheets', 'Income Statements']
    #     sample = self.engine.get_statements(years, statements, company='DINAMOW')
    #     # print(sample)