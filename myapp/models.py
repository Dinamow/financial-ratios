from django.db import models
import json
from math import sqrt


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
    number_of_shares = models.FloatField(verbose_name="Number of Shares",
                                         default=0.0)
    market_price = models.FloatField(verbose_name="Market Price",
                                     default=0.0)
    net_income = models.FloatField(verbose_name="Net Income",
                                   default=0.0)
    sales = models.FloatField(verbose_name="Sales",
                              default=0.0)
    total_assets = models.FloatField(verbose_name="Total Assets",
                                     default=0.0)
    total_equity = models.FloatField(verbose_name="Total Equity",
                                     default=0.0)
    ebit = models.FloatField(verbose_name="EBIT",
                             default=0.0)
    intrest = models.FloatField(verbose_name="Interest Expense",
                                default=0.0)
    tax_rate = models.FloatField(verbose_name="Tax Rate",
                                 default=0.0)
    dividans = models.FloatField(verbose_name="Dividans",
                                 default=0.0)
    total_fixed_assets = models.FloatField(verbose_name="Fixed Assets",
                                           default=0.0)
    total_current_assets = models.FloatField(verbose_name="Total Current Assets",
                                             default=0.0)
    cogs = models.FloatField(verbose_name="Cost of Revenue, Total",
                             default=0.0)
    inventory = models.FloatField(verbose_name="Total Inventory",
                                  default=0.0)
    account_recivables = models.FloatField(verbose_name="Total Receivables, Net",
                                           default=0.0)
    account_payable = models.FloatField(verbose_name="Accounts Payable",
                                        default=0.0)
    cash = models.FloatField(verbose_name="Cash & Equivalents",
                             default=0.0)
    total_current_liabilty = models.FloatField(verbose_name="Total Current Liabilities",
                                               default=0.0)
    total_debt = models.FloatField(verbose_name="Total Debt",
                                   default=0.0)
    ebitida = models.FloatField(verbose_name="EBITDA",
                                default=0.0)
    dividansRatio = models.FloatField(verbose_name="Dividans Ratio",
                                      default=models.F('dividans') / models.F('net_income'),
                                      editable=False)
    book_value = models.FloatField(verbose_name="Book Value",
                                   default=models.F('equity') / models.F('number_of_shares'),
                                   editable=False)
    eps = models.FloatField(verbose_name="EPS",
                            default=models.F('net_income') / models.F('number_of_shares'),
                            editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company.name + " " + self.date.date

class Lequidity():
    """lequidity class"""

    def get_current_ratio_value(self):
        """return current ratio value"""
        return {
            "value": round((
                self._cash +
                self._account_recivables +
                self._inventory) /
            self._total_current_liabilty, 2)}

    def get_current_ratio_fourmula(self):
        """return current ratio formula"""
        numbers = f"({self._cash} + {self._account_recivables}"
        numbers += f" + {self._inventory}) / {self._total_current_liabilty}"
        return {
            "formula": {
                "rule": "cash + AR + INV / CL",
                "numbers": f"{numbers}"}}

    def get_quick_ratio_value(self):
        """return quick ratio value"""
        return {
            "value": round(
            (self._cash + self._account_recivables) / self._total_current_liabilty, 2)
        }

    def get_quick_ratio_fourmula(self):
        """return quick ratio formula"""
        numbers = f"({self._cash}"
        numbers += f" + {self._account_recivables}) / {self._total_current_liabilty}"
        return {
            "formula": {
                "rule": "cash + AR / CL",
                "numbers": f"{numbers}"}}

    def get_cash_ratio_value(self):
        """return cash ratio value"""
        return {"value": round(self._cash / self._total_current_liabilty, 2)}

    def get_cash_ratio_fourmula(self):
        """return cash ratio formula"""
        return {
            "formula": {
                "rule": "cash / CL",
                "numbers": f"{self._cash} / {self._total_current_liabilty}"}}


class Leveraging():
    """leverage class"""

    def get_debt_ratio_value(self):
        """return debt ratio value"""
        return {"value": round(self._total_debt / self._total_assets, 2)}

    def get_debt_ratio_fourmula(self):
        """return debt ratio formula"""
        return {
            "formula": {
                "rule": "TD / TA",
                "numbers": f"{self._total_debt} / {self._total_assets}"}}

    def get_debt_equity_ratio_value(self):
        """return debt equity ratio value"""
        return {"value": round(self._total_debt / self._total_equity, 2)}

    def get_debt_equity_ratio_fourmula(self):
        """return debt equity ratio formula"""
        return {
            "formula": {
                "rule": "TD / TE",
                "numbers": f"{self._total_debt} / {self._total_equity}"}}

    def get_equity_multiplier_value(self):
        """return equity multiplier value"""
        return {"value": round(self._total_assets / self._total_equity, 2)}

    def get_equity_multiplier_fourmula(self):
        """return equity multiplier formula"""
        return {
            "formula": {
                "rule": "TA / TE",
                "numbers": f"{self._total_assets} / {self._total_equity}"}}

    def get_times_interest_earned_value(self):
        """return times interest earned value"""
        return {"value": round(self._ebit / self._intrest, 2)}

    def get_times_interest_earned_fourmula(self):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self._ebit} / {self._intrest}"}}

    def get_ebitda_coverage_value(self):
        """return EBITDA coverage value"""
        return {"value": round(self._ebitda / self._intrest, 2)}

    def get_ebitda_coverage_fourmula(self):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self._ebitda} / {self._intrest}"}}


class AssetsTO():
    """assets turn over class"""

    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": round(self._sales / self._total_assets, 2)}

    def get_total_assets_turnover_fourmula(self):
        """return total assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / TA",
                "numbers": f"{self._sales} / {self._total_assets}"}}

    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": round(self._sales / self._total_fixed_assets, 2)}

    def get_fixed_assets_turnover_fourmula(self):
        """return fixed assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / FA",
                "numbers": f"{self._sales} / {self._total_fixed_assets}"}}

    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": round(self._sales / self._total_current_assets, 2)}

    def get_current_assets_turnover_fourmula(self):
        """return current assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / CA",
                "numbers": f"{self._sales} / {self._total_current_assets}"}}

    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": round(self._cogs / self._inventory, 2)}

    def get_inventory_turnover_fourmula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self._cogs} / {self._inventory}"}}

    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": round(self._inventory / self._cogs * 365, 2)}

    def get_days_sales_in_inventory_fourmula(self):
        """return days sales in inventory formula"""
        return {
            "formula": {
                "rule": "INV / COGS * 365",
                "numbers": f"{self._inventory} / {self._cogs} * 365"}}

    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": round(self._sales / self._account_recivables, 2)}

    def get_receivables_turnover_fourmula(self):
        """return receivables turnover formula"""
        return {
            "formula": {
                "rule": "Sales / AR",
                "numbers": f"{self._sales} / {self._account_recivables}"}}

    def get_days_sales_in_receivables_value(self):
        """return days sales in receivables value"""
        return {"value": round(self._account_recivables / self._sales * 365, 2)}

    def get_days_sales_in_receivables_fourmula(self):
        """return days sales in receivables formula"""
        numbers = f"{self._account_recivables} / {self._sales} * 365"
        return {
            "formula": {
                "rule": "AR / Sales * 365",
                "numbers": f"{numbers}"}}

    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": round(self._cogs / self._account_payable, 2)}

    def get_payables_turnover_fourmula(self):
        """return payables turnover formula"""
        return {
            "formula": {
                "rule": "COGS / AP",
                "numbers": f"{self._cogs} / {self._account_payable}"}}


class Profitability(Leveraging):

    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": round(self._net_income / self._sales, 2)}

    def get_net_profit_margin_fourmula(self):
        """return net profit margin formula"""
        return {"formula": {"rule": "NI / Sales",
                            "numbers": f"{self._net_income} / {self._sales}"}}

    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": round(self._net_income / self._total_assets, 2)}

    def get_return_on_assets_fourmula(self):
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

    def get_return_on_equity_fourmula(self):
        """return return on equity formula"""
        return {
            "formula": {
                "rule": "NI / TE",
                "numbers": f"{self._net_income} / {self._total_equity}",
                "rule": "ROA * EM",
                "numbers": f"{self.get_return_on_assets_value()['value']} * {self.get_equity_multiplier_value()['value']}"}}

    def get_roi_value(self):
        """return ROI value"""
        self._roi = self._ebit / self._total_assets
        return {"value": round(self._ebit / self._total_assets, 2)}

    def get_roi_fourmula(self):
        """return ROI formula"""
        return {
            "formula": {
                "rule": "EBIT / TA",
                "numbers": f"{self._ebit} / {self._total_assets}"}}

    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {
            "value": round(
            (self.get_roi_value()['value'] - self._intrest) *
            self.get_debt_equity_ratio_value()['value'], 2)
        }

    def get_return_trade_on_equity_fourmula(self):
        """return return trade on equity formula"""
        return {
            "formula": {
                "rule": "(ROI - IE) * DER",
                "numbers": f"({self.get_roi_value()['value']} - {self._intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_ROE_using_EOV_value(self):
        """return ROE using EOV"""
        self.get_roi_value()
        return {"value": round((1 -
                          self._tax_rate) *
                self._roi +
                (self._roi -
                 self._intrest) *
                self.get_debt_equity_ratio_value()['value'], 2)}

    def get_ROE_using_EOV_fourmula(self):
        """return ROE using EOV formula"""
        return {
            "formula": {
                "rule": "(1 - T) * ROI + (ROI - IE) * DER",
                "numbers": f"(1 - {self._tax_rate}) * {self._roi} + ({self._roi} - {self._intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": round(self.get_return_on_assets_value(
        )['value'] * (1 - self._dividansRatio), 2)}


class MarketValue():

    def get_eps_value(self):
        """return EPS value"""
        return {"value": round(self._eps, 2)}

    def get_eps_fourmula(self):
        """return EPS formula"""
        return {"formula": {"rule": "NI / Number of Shares",
                            "numbers": f"{self._net_income} / {self._number_of_shares}"}}

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": round(self._market_price / self._eps, 2)}

    def get_pe_ratio_fourmula(self):
        """return PE ratio formula"""
        return {"formula": {"rule": "Market Price / EPS",
                            "numbers": f"{self._market_price} / {self._eps}"}}

    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": round(self._market_price / self._book_value, 2)}

    def get_mb_ratio_fourmula(self):
        """return PB ratio formula"""
        return {"formula": {"rule": "Market Price / Book Value",
                            "numbers": f"{self._market_price} / {self._book_value}"}}

    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": round(sqrt(1.5 * 15 * self._book_value * self._eps), 2)}


class Engine(Lequidity, AssetsTO, Profitability, MarketValue):
    """engine class"""
    _data = None

    def __init__(self) -> None:
        super().__init__()
        self._data = json.load(open('company.json'))

    def get_dates(self):
        """return dates"""
        return list(self._data['Financial Statements']['Balance Sheets'])

    def date(self, year):
        self._number_of_shares = self._data['Financial Statements'][
            'Income Statements'][year]['Number of Shares']
        self._market_price = self._data['Financial Statements'][
            'Income Statements'][year]['Market Price']
        self._net_income = self._data['Financial Statements'][
            'Income Statements'][year]['Net Income']
        self._sales = self._data['Financial Statements'][
            'Income Statements'][year]['Sales']
        self._total_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._total_equity = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Equity']
        self._ebit = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._intrest = self._data['Financial Statements'][
            'Income Statements'][year]['Interest Expense']
        self._tax_rate = self._data['Financial Statements'][
            'Income Statements'][year]['Tax Rate']
        self._dividansRatio = self._data['Financial Statements'][
            'Income Statements'][year]['Dividans Ratio']
        self._total_fixed_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Fixed Assets']
        self._total_current_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Current Assets']
        self._cogs = self._data['Financial Statements'][
            'Income Statements'][year]['Cost of Revenue, Total']
        self._inventory = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Inventory']
        self._account_recivables = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Receivables, Net']
        self._account_payable = self._data['Financial Statements'][
            'Balance Sheets'][year]['Accounts Payable']
        self._cash = self._data['Financial Statements'][
            'Balance Sheets'][year]['Cash & Equivalents']
        self._total_current_liabilty = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Current Liabilities']
        self._total_debt = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Debt']
        self._total_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._EBIT = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._ebitda = self._data['Financial Statements'][
            'Income Statements'][year]['EBITDA']
        self._book_value = self._equity / self._number_of_shares
        self._eps = self._net_income / self._number_of_shares
