from django.test import TestCase
from .models import Engine


# Create your tests here.
class MyTests(TestCase):
    
    def setUp(self):
        self.engine = Engine()
    
    def test_testing(self):
        """test the testing view"""
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'foo': 'bar'})
    
    def test_dates(self):
        """test the dates view"""
        response = self.client.get('/api/v1/dates/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['dates'], self.engine.get_dates())
    
    def test_get_current_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_current_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_cash_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_cash_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_debt_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_debt_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_debt_equity_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_debt_equity_ratio_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_equity_multiplier_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_equity_multiplier_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_times_interest_earned_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_times_interest_earned_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_ebitda_coverage_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_ebitda_coverage_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_total_assets_turnover_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_total_assets_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_current_assets_turnover_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_current_assets_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_inventory_turnover_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_inventory_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_days_sales_in_inventory_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_days_sales_in_inventory_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_receivables_turnover_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_receivables_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_days_sales_in_receivables_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_days_sales_in_receivables_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_payables_turnover_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_payables_turnover_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_net_profit_margin_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_net_profit_margin_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_return_on_assets_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_return_on_assets_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_return_on_equity_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_return_on_equity_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_roi_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_roi_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_return_trade_on_equity_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_return_trade_on_equity_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_ROE_using_EOV_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_ROE_using_EOV_value()
        self.assertNotEqual(ca, 0.0)
    
    def test_get_internal_growth_rate_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_internal_growth_rate_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_eps_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_eps_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_pe_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_pe_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_mb_ratio_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_mb_ratio_value()
        self.assertNotEqual(ca, 0.0)

    def test_get_fair_value_of_stock_value(self):
        """test the balance view"""
        self.engine.date('2023')
        ca = self.engine.get_fair_value_of_stock_value()
        self.assertNotEqual(ca, 0.0)

