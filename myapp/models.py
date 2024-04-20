from django.db import models
from math import sqrt
import re


# Create your models here.
class Dates(models.Model):
    db_table = 'dates'
    date = models.CharField(max_length=10,
                            verbose_name="Date",
                            unique=True)
    
    def __str__(self) -> str:
        return self.date

class Company(models.Model):
    db_table = 'companies'
    name = models.CharField(max_length=100,
                            verbose_name="Company Name",
                            unique=True)
    
    def __str__(self) -> str:
        return self.name

class Ratios(models.Model):
    db_table = 'ratios'
    number_of_shares = models.FloatField(verbose_name="Number of Shares", default=0.0)
    market_price = models.FloatField(verbose_name="Market Price", default=0.0)
    net_income = models.FloatField(verbose_name="Net Income", default=0.0)
    sales = models.FloatField(verbose_name="Sales", default=0.0)
    total_assets = models.FloatField(verbose_name="Total Assets", default=0.0)
    total_equity = models.FloatField(verbose_name="Total Equity", default=0.0)
    ebit = models.FloatField(verbose_name="EBIT", default=0.0)
    interest = models.FloatField(verbose_name="Interest Expense", default=0.0)
    tax_rate = models.FloatField(verbose_name="Tax Rate", default=0.0)
    dividends = models.FloatField(verbose_name="Dividends", default=0.0)
    total_fixed_assets = models.FloatField(verbose_name="Fixed Assets", default=0.0)
    total_current_assets = models.FloatField(verbose_name="Total Current Assets", default=0.0)
    cogs = models.FloatField(verbose_name="Cost of Revenue, Total", default=0.0)
    inventory = models.FloatField(verbose_name="Total Inventory", default=0.0)
    account_receivables = models.FloatField(verbose_name="Total Receivables, Net", default=0.0)
    account_payable = models.FloatField(verbose_name="Accounts Payable", default=0.0)
    cash = models.FloatField(verbose_name="Cash & Equivalents", default=0.0)
    total_current_liability = models.FloatField(verbose_name="Total Current Liabilities", default=0.0)
    total_debt = models.FloatField(verbose_name="Total Debt", default=0.0)
    ebitda = models.FloatField(verbose_name="EBITDA", default=0.0)
    dividansRatio = models.FloatField(verbose_name="Dividans Ratio", default=0.0,
                                      editable=False)
    book_value = models.FloatField(verbose_name="Book Value", default=0.0,
                                   editable=False)
    eps = models.FloatField(verbose_name="EPS", default=0.0,
                            editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Calculate dividansRatio
        if self.net_income != 0:
            self.dividansRatio = self.dividends / self.net_income
        else:
            self.dividansRatio = 0.0
        
        # Calculate book_value
        if self.number_of_shares != 0:
            self.book_value = self.total_equity / self.number_of_shares
        else:
            self.book_value = 0.0
        
        # Calculate eps
        if self.number_of_shares != 0:
            self.eps = self.net_income / self.number_of_shares
        else:
            self.eps = 0.0
        
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.company.name + ' - ' + self.date.date

class Lequidity():
    """lequidity class"""

    def get_current_ratio_value(self):
        """return current ratio value"""
        return {
            "value": round((
                self._cash +
                self._account_receivables +
                self._inventory) /
            self._total_current_liability, 2)}

    def get_current_ratio_formula(self):
        """return current ratio formula"""
        numbers = f"({self._cash} + {self._account_receivables}"
        numbers += f" + {self._inventory}) / {self._total_current_liability}"
        return {
            "formula": {
                "rule": "cash + AR + INV / CL",
                "numbers": f"{numbers}"}}

    def get_quick_ratio_value(self):
        """return quick ratio value"""
        return {
            "value": round(
            (self._cash + self._account_receivables) / self._total_current_liability, 2)}

    def get_quick_ratio_formula(self):
        """return quick ratio formula"""
        numbers = f"({self._cash}"
        numbers += f" + {self._account_receivables}) / {self._total_current_liability}"
        return {
            "formula": {
                "rule": "cash + AR / CL",
                "numbers": f"{numbers}"}}

    def get_cash_ratio_value(self):
        """return cash ratio value"""
        return {"value": round(self._cash / self._total_current_liability, 2)}

    def get_cash_ratio_formula(self):
        """return cash ratio formula"""
        return {
            "formula": {
                "rule": "cash / CL",
                "numbers": f"{self._cash} / {self._total_current_liability}"}}

class Leveraging():
    """leverage class"""

    def get_debt_ratio_value(self):
        """return debt ratio value"""
        return {"value": round(self._total_debt / self._total_assets, 2)}

    def get_debt_ratio_formula(self):
        """return debt ratio formula"""
        return {
            "formula": {
                "rule": "TD / TA",
                "numbers": f"{self._total_debt} / {self._total_assets}"}}

    def get_debt_equity_ratio_value(self):
        """return debt equity ratio value"""
        return {"value": round(self._total_debt / self._total_equity, 2)}

    def get_debt_equity_ratio_formula(self):
        """return debt equity ratio formula"""
        return {
            "formula": {
                "rule": "TD / TE",
                "numbers": f"{self._total_debt} / {self._total_equity}"}}

    def get_equity_multiplier_value(self):
        """return equity multiplier value"""
        return {"value": round(self._total_assets / self._total_equity, 2)}

    def get_equity_multiplier_formula(self):
        """return equity multiplier formula"""
        return {
            "formula": {
                "rule": "TA / TE",
                "numbers": f"{self._total_assets} / {self._total_equity}"}}

    def get_times_interest_earned_value(self):
        """return times interest earned value"""
        return {"value": round(self._ebit / self._interest, 2)}

    def get_times_interest_earned_formula(self):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self._ebit} / {self._interest}"}}

    def get_ebitda_coverage_value(self):
        """return EBITDA coverage value"""
        return {"value": round(self._ebitda / self._interest, 2)}

    def get_ebitda_coverage_formula(self):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self._ebitda} / {self._interest}"}}

class AssetsTO():
    """assets turn over class"""

    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": round(self._sales / self._total_assets, 2)}

    def get_total_assets_turnover_formula(self):
        """return total assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / TA",
                "numbers": f"{self._sales} / {self._total_assets}"}}

    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": round(self._sales / self._total_fixed_assets, 2)}

    def get_fixed_assets_turnover_formula(self):
        """return fixed assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / FA",
                "numbers": f"{self._sales} / {self._total_fixed_assets}"}}

    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": round(self._sales / self._total_current_assets, 2)}

    def get_current_assets_turnover_formula(self):
        """return current assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / CA",
                "numbers": f"{self._sales} / {self._total_current_assets}"}}

    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": round(self._cogs / self._inventory, 2)}

    def get_inventory_turnover_formula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self._cogs} / {self._inventory}"}}

    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": round(self._inventory / self._cogs * 365, 2)}

    def get_days_sales_in_inventory_formula(self):
        """return days sales in inventory formula"""
        return {
            "formula": {
                "rule": "INV / COGS * 365",
                "numbers": f"{self._inventory} / {self._cogs} * 365"}}

    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": round(self._sales / self._account_receivables, 2)}

    def get_receivables_turnover_formula(self):
        """return receivables turnover formula"""
        return {
            "formula": {
                "rule": "Sales / AR",
                "numbers": f"{self._sales} / {self._account_receivables}"}}

    def get_days_sales_outstanding_value(self):
        """return days sales in receivables value"""
        return {"value": round(self._account_receivables / self._sales * 365, 2)}

    def get_days_sales_outstanding_formula(self):
        """return days sales in receivables formula"""
        numbers = f"{self._account_receivables} / {self._sales} * 365"
        return {
            "formula": {
                "rule": "AR / Sales * 365",
                "numbers": f"{numbers}"}}

    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": round(self._cogs / self._account_payable, 2)}

    def get_payables_turnover_formula(self):
        """return payables turnover formula"""
        return {
            "formula": {
                "rule": "COGS / AP",
                "numbers": f"{self._cogs} / {self._account_payable}"}}
    
    def get_paid_period_value(self):
        """return paid period value"""
        return {"value": round(self._account_payable / self._cogs * 365, 2)}
    
    def get_paid_period_formula(self):
        """return paid period formula"""
        return {
            "formula": {
                "rule": "AP / COGS * 365",
                "numbers": f"{self._account_payable} / {self._cogs} * 365"}}

class Profitability(Leveraging):

    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": round(self._net_income / self._sales, 2)}

    def get_net_profit_margin_formula(self):
        """return net profit margin formula"""
        return {"formula": {"rule": "NI / Sales",
                            "numbers": f"{self._net_income} / {self._sales}"}}

    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": round(self._net_income / self._total_assets, 2)}

    def get_return_on_assets_formula(self):
        """return return on assets formula"""
        return {
            "formula": {
                "rule": "NI / TA",
                "numbers": f"{self._net_income} / {self._total_assets}",
                "rule": "TOTA * PM",
                "numbers": f"{self._total_assets} * {self.get_net_profit_margin_value()['value']}"}}

    def get_return_on_equity_value(self):
        """return return on equity value"""
        return {"value": round(self._net_income / self._total_equity, 2)}

    def get_return_on_equity_formula(self):
        """return return on equity formula"""
        return {
            "formula": {
                "rule": "NI / TE",
                "numbers": f"{self._net_income} / {self._total_equity}",
                "rule": "ROA * EM",
                "numbers": f"{self.get_return_on_assets_value()['value']} * {self.get_equity_multiplier_value()['value']}"}}

    def get_return_on_investment_value(self):
        """return return on investment value"""
        self._roi = self._ebit / self._total_assets
        return {"value": round(self._ebit / self._total_assets, 2)}

    def get_return_on_investment_formula(self):
        """return return on investment formula"""
        return {
            "formula": {
                "rule": "EBIT / TA",
                "numbers": f"{self._ebit} / {self._total_assets}"}}

    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {
            "value": round(
            (self.get_return_on_investment_value()['value'] - self._interest) *
            self.get_debt_equity_ratio_value()['value'], 2)
        }

    def get_return_trade_on_equity_formula(self):
        """return return trade on equity formula"""
        return {
            "formula": {
                "rule": "(ROI - IE) * DER",
                "numbers": f"({self.get_return_on_investment_value()['value']} - {self._interest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_return_trade_on_equity_using_eva_value(self):
        """return return trade on equity using eva"""
        self.get_return_on_investment_value()
        return {"value": round((1 -
                          self._tax_rate) *
                self._roi +
                (self._roi -
                 self._interest) *
                self.get_debt_equity_ratio_value()['value'], 2)}

    def get_return_trade_on_equity_using_eva_formula(self):
        """return return trade on equity using eva formula"""
        return {
            "formula": {
                "rule": "(1 - T) * ROI + (ROI - IE) * DER",
                "numbers": f"(1 - {self._tax_rate}) * {self._roi} + ({self._roi} - {self._interest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": round(self.get_return_on_assets_value(
        )['value'] * (1 - self._dividends_ratio), 2)}
    
    def get_internal_growth_rate_formula(self):
        """return internal growth rate formula"""
        return {
            "formula": {
                "rule": "ROA * (1 - DR)",
                "numbers": f"{self.get_return_on_assets_value()['value']} * (1 - {self._dividends_ratio})"}}
    
    def get_sustainable_growth_rate_value(self):
        """return sustainable growth rate value"""
        return {"value": round(self.get_return_on_assets_value(
        )['value'] * (1 - self._dividends_ratio), 2)}

    def get_sustainable_growth_rate_formula(self):
        """return sustainable growth rate formula"""
        return {
            "formula": {
                "rule": "ROA * (1 - DR)",
                "numbers": f"{self.get_return_on_assets_value()['value']} * (1 - {self._dividends_ratio})"}}

class MarketValue():

    def get_eps_value(self):
        """return EPS value"""
        return {"value": round(self._eps, 2)}

    def get_eps_formula(self):
        """return EPS formula"""
        return {"formula": {"rule": "NI / Number of Shares",
                            "numbers": f"{self._net_income} / {self._number_of_shares}"}}

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": round(self._market_price / self._eps, 2)}

    def get_pe_ratio_formula(self):
        """return PE ratio formula"""
        return {"formula": {"rule": "Market Price / EPS",
                            "numbers": f"{self._market_price} / {self._eps}"}}

    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": round(self._market_price / self._book_value, 2)}

    def get_mb_ratio_formula(self):
        """return PB ratio formula"""
        return {"formula": {"rule": "Market Price / Book Value",
                            "numbers": f"{self._market_price} / {self._book_value}"}}

    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": sqrt(1.5 * 15 * self._book_value * self._eps)}

    def get_fair_value_of_stock_formula(self):
        """return fair value of stock formula"""
        return {
            "formula": {
                "rule": "sqrt(1.5 * 15 * BV * EPS)",
                "numbers": f"sqrt(1.5 * 15 * {self._book_value} * {self._eps})"}}

class Engine(Lequidity, AssetsTO, Profitability, MarketValue):
    """engine class"""

    def __init__(self):
        self.__RATIOSLIST = {
            'liquidity': [
                'Current Ratio',
                'Quick Ratio',
                'Cash Ratio'
            ],
            'leverage': [
                'Debt Ratio',
                'Debt Equity Ratio',
                'Equity Multiplier',
                'Times Interest Earned',
                'EBITDA Coverage'
            ],
            'assetsto': [
                'Total Assets Turnover',
                'Fixed Assets Turnover',
                'Current Assets Turnover',
                'Inventory Turnover',
                'Days Sales in Inventory',
                'Receivables Turnover',
                'Days Sales Outstanding',
                'Payables Turnover',
                'Paid Period'
            ],
            'profitability': [
                'Net Profit Margin',
                'Return on Assets',
                'Return on Equity',
                'Return on Investment',
                'Return Trade on Equity',
                'Return Trade on Equity using EVA',
                'Internal Growth Rate',
                'sustainable Growth Rate'
            ],
            'marketvalue': [
                'EPS',
                'PE Ratio',
                'MB Ratio',
                'Fair Value of Stock'
            ]
        }
        self.__RAWDATA = [
            'Number of Shares',
            'Market Price',
            'Net Income',
            'Sales',
            'Total Assets',
            'Total Equity',
            'EBIT',
            'Interest',
            'Tax Rate',
            'Dividends Ratio',
            'Total Fixed Assets',
            'Total Current Assets',
            'COGS',
            'Inventory',
            'Account Receivables',
            'Account Payable',
            'Cash',
            'Total Current Liability',
            'Total Debt',
            'EBITDA',
            'Book Value',
            'EPS'
        ]

    def get_dates(self):
        """return dates"""
        companies = Company.objects.all()
        data = []

        for company in companies:
            company_data = {
                'company': company.name,
                'Dates': list(Ratios.objects.filter(company=company).values_list('date__date', flat=True).distinct())
            }
            data.append(company_data)
        return data

    def date(self, year, company):
        year = Dates.objects.filter(date=year).first()
        company_id = Company.objects.filter(name=company).first()
        if not year or not company_id:
            return None
        self._number_of_shares = Ratios.objects.get(date=year, company_id=company_id).number_of_shares
        self._market_price = Ratios.objects.get(date=year, company_id=company_id).market_price
        self._net_income = Ratios.objects.get(date=year, company_id=company_id).net_income
        self._sales = Ratios.objects.get(date=year, company_id=company_id).sales
        self._total_assets = Ratios.objects.get(date=year, company_id=company_id).total_assets
        self._total_equity = Ratios.objects.get(date=year, company_id=company_id).total_equity
        self._ebit = Ratios.objects.get(date=year, company_id=company_id).ebit
        self._interest = Ratios.objects.get(date=year, company_id=company_id).interest
        self._tax_rate = Ratios.objects.get(date=year, company_id=company_id).tax_rate
        self._dividends_ratio = Ratios.objects.get(date=year, company_id=company_id).dividansRatio
        self._total_fixed_assets = Ratios.objects.get(date=year, company_id=company_id).total_fixed_assets
        self._total_current_assets = Ratios.objects.get(date=year, company_id=company_id).total_current_assets
        self._cogs = Ratios.objects.get(date=year, company_id=company_id).cogs
        self._inventory = Ratios.objects.get(date=year, company_id=company_id).inventory
        self._account_receivables = Ratios.objects.get(date=year, company_id=company_id).account_receivables
        self._account_payable = Ratios.objects.get(date=year, company_id=company_id).account_payable
        self._cash = Ratios.objects.get(date=year, company_id=company_id).cash
        self._total_current_liability = Ratios.objects.get(date=year, company_id=company_id).total_current_liability
        self._total_debt = Ratios.objects.get(date=year, company_id=company_id).total_debt
        self._ebitda = Ratios.objects.get(date=year, company_id=company_id).ebitda
        self._book_value = self._total_equity / self._number_of_shares
        self._eps = self._net_income / self._number_of_shares

    def get_raw_data(self, years, company):
        """return raw data (which is used to get ratios)"""
        raw_data = {}
        for year in years:
            self.date(year, company)
            raw_data[year] = {data: getattr(self, f"_{data.lower().replace(' ', '_')}") for data in self.__RAWDATA}
        return raw_data

    def get_date_ratios(self, year, company):
        """return date ratios"""
        self.date(year, company)

        ratios_info = {}
        for ratios in self.__RATIOSLIST.values():
            for ratio in ratios:
                ratio_data = {
                    'value': getattr(self, f"get_{ratio.lower().replace(' ', '_')}_value")()['value'],
                    'formula': getattr(self, f"get_{ratio.lower().replace(' ', '_')}_formula")()['formula']
                }
                ratios_info[ratio] = ratio_data

        return ratios_info

    def get_components(self, formula):
        formula = str(formula).replace("sqrt", "")
        components = re.findall(r'\b[\w.]+\b', str(formula))
        return components

    def get_components_values(self, numbers):
        components_values = re.findall(r'\d+\.\d+|\d+', str(numbers))
        return components_values

    def get_ratio(self, ratio, years, company):
        """return ratio"""
        formula = self.get_date_ratios(years[0], company)[ratio]['formula']
        components: str = self.get_components(formula['rule'])
        ratio_info = {
            'ratio': ratio,
            'formula': formula['rule'],
            'components': components,
        }
        for year in years:
            ratio_info[year] = {
            'value': self.get_date_ratios(year, company)[ratio]['value'],
            'numbers': self.get_date_ratios(year, company)[ratio]['formula']['numbers'],
            }
            year_components_values = self.get_components_values(ratio_info[year]['numbers'])
            components_with_values = dict(zip(components, year_components_values))
            ratio_info[year].update(components_with_values)
        return ratio_info

    def get_type(self, type, years, company):
        """return type"""
        
        if type not in self.__RATIOSLIST.keys():
            return {"error": "Invalid type",
                    "types": list(self.__RATIOSLIST.keys())}
        
        ratios = self.__RATIOSLIST[type]
        
        if not years:
            return {"error": "Please provide years"}

        type_ratios = {}
        if len(years) == 1:
            year = years[0]
            type_ratios[year] = []
            for ratio in ratios:
                ratio_info = {
                    'type': ratio,
                    'value': self.get_date_ratios(year, company)[ratio]['value'],
                    'formula': self.get_date_ratios(year, company)[ratio]['formula']['rule'],
                    'numbers': self.get_date_ratios(year, company)[ratio]['formula']['numbers']
                }
                type_ratios[year].append(ratio_info)
        else:
            type_ratios = {
                'ratios': ratios,
            }
            for year in years:
                type_ratios[year] = {
                    ratio: self.get_date_ratios(year, company)[ratio]['value'] for ratio in ratios
                }
        return type_ratios
