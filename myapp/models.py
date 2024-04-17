from django.db import models
import json
import math


# Create your models here.
class Lequidity():
    """lequidity class"""
    __data = None
    __cash = None
    __ar = None
    __inv = None
    __cl = None
    
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    @property
    def date(self, year):
        self.__cash = self.__data['Financial Statements']['Balance Sheets'][year]['Cash & Equivalents']
        self.__ar = self.__data['Financial Statements']['Balance Sheets'][year]['Accounts Receivable']
        self.__inv = self.__data['Financial Statements']['Balance Sheets'][year]['Inventory']
        self.__cl = self.__data['Financial Statements']['Balance Sheets'][year]['Current Liabilities']
    
    def get_current_ratio_value(self):
        """return current ratio value"""
        return {"value": (self.__cash + self.__ar + self.__inv) / self.__cl}
    
    def get_current_ratio_fourmula(self):
        """return current ratio formula"""
        return {"formula": {"rule": "cash + AR + INV / CL",
                            "numbers": f"({self.__cash} + {self.__ar} + {self.__inv}) / {self.__cl}"}}
    
    def get_quick_ratio_value(self):
        """return quick ratio value"""
        return {"value": (self.__cash + self.__ar) / self.__cl}
    
    def get_quick_ratio_fourmula(self):
        """return quick ratio formula"""
        return {"formula": {"rule": "cash + AR / CL",
                            "numbers": f"({self.__cash} + {self.__ar}) / {self.__cl}"}}
    
    def get_cash_ratio_value(self):
        """return cash ratio value"""
        return {"value": self.__cash / self.__cl}
    
    def get_cash_ratio_fourmula(self):
        """return cash ratio formula"""
        return {"formula": {"rule": "cash / CL",
                            "numbers": f"{self.__cash} / {self.__cl}"}}


class Leveraging():
    """leverage class"""
    __TD = None
    __TE = None
    __TA = None
    __EBIT = None
    __IE = None
    __EBITDA = None

    
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    @property
    def date(self, year):
        self.__TD = self.__data['Financial Statements']['Balance Sheets'][year]['total debt']
        self.__TE = self.__data['Financial Statements']['Balance Sheets'][year]['Total Equity']
        self.__TA = self.__data['Financial Statements']['Balance Sheets'][year]['Total Assets']
        self.__EBIT = self.__data['Financial Statements']['Income Statements'][year]['EBIT']
        self.__IE = self.__data['Financial Statements']['Income Statements'][year]['Interest Expense']
        self.__EBITDA = self.__data['Financial Statements']['Income Statements'][year]['EBITDA']
    
    def get_debt_ratio_value(self, year):
        """return debt ratio value"""
        return {"value": self.__TD / self.__TA}
    
    def get_debt_ratio_fourmula(self, year):
        """return debt ratio formula"""
        return {"formula": {"rule": "TD / TA",
                            "numbers": f"{self.__TD} / {self.__TA}"}}
    
    def get_debt_equity_ratio_value(self, year):
        """return debt equity ratio value"""
        return {"value": self.__TD / self.__TE}
    
    def get_debt_equity_ratio_fourmula(self, year):
        """return debt equity ratio formula"""
        return {"formula": {"rule": "TD / TE",
                            "numbers": f"{self.__TD} / {self.__TE}"}}
    
    def get_equity_multiplier_value(self, year):
        """return equity multiplier value"""
        return {"value": self.__TA / self.__TE}
    
    def get_equity_multiplier_fourmula(self, year):
        """return equity multiplier formula"""
        return {"formula": {"rule": "TA / TE",
                            "numbers": f"{self.__TA} / {self.__TE}"}}
    
    def get_times_interest_earned_value(self, year):
        """return times interest earned value"""
        return {"value": self.__EBIT / self.__IE}
    
    def get_times_interest_earned_fourmula(self, year):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self.__EBIT} / {self.__IE}"}}
    
    def get_ebitda_coverage_value(self, year):
        """return EBITDA coverage value"""
        return {"value": self.__EBITDA / self.__IE}
    
    def get_ebitda_coverage_fourmula(self, year):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self.__EBITDA} / {self.__IE}"}}


class AssetsTO():
    """assets turn over class"""
    __sales = None
    __ta = None
    __fa = None
    __ca = None
    __cogs = None
    __inv = None
    __ar = None
    __ap = None
    
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    @property
    def date(self, year):
        self.__sales = self.__data['Financial Statements']['Income Statements'][year]['Sales']
        self.__ta = self.__data['Financial Statements']['Balance Sheets'][year]['Total Assets']
        self.__fa = self.__data['Financial Statements']['Balance Sheets'][year]['Fixed Assets']
        self.__ca = self.__data['Financial Statements']['Balance Sheets'][year]['Current Assets']
        self.__cogs = self.__data['Financial Statements']['Income Statements'][year]['COGS']
        self.__inv = self.__data['Financial Statements']['Balance Sheets'][year]['Inventory']
        self.__ar = self.__data['Financial Statements']['Balance Sheets'][year]['Accounts Receivable']
        self.__ap = self.__data['Financial Statements']['Balance Sheets'][year]['Accounts Payable']
    
    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": self.__sales / self.__ta}
    
    def get_total_assets_turnover_fourmula(self):
        """return total assets turnover formula"""
        return {"formula": {"rule": "Sales / TA",
                            "numbers": f"{self.__sales} / {self.__ta}"}}
    
    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": self.__sales / self.__fa}
    
    def get_fixed_assets_turnover_fourmula(self):
        """return fixed assets turnover formula"""
        return {"formula": {"rule": "Sales / FA",
                            "numbers": f"{self.__sales} / {self.__fa}"}}
    
    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": self.__sales / self.__ca}
    
    def get_current_assets_turnover_fourmula(self):
        """return current assets turnover formula"""
        return {"formula": {"rule": "Sales / CA",
                            "numbers": f"{self.__sales} / {self.__ca}"}}
    
    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": self.__cogs / self.__inv}
    
    def get_inventory_turnover_fourmula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self.__cogs} / {self.__inv}"}}
    
    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": self.__inv / self.__cogs * 365}
    
    def get_days_sales_in_inventory_fourmula(self):
        """return days sales in inventory formula"""
        return {"formula": {"rule": "INV / COGS * 365",
                            "numbers": f"{self.__inv} / {self.__cogs} * 365"}}
    
    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": self.__sales / self.__ar}
    
    def get_receivables_turnover_fourmula(self):
        """return receivables turnover formula"""
        return {"formula": {"rule": "Sales / AR",
                            "numbers": f"{self.__sales} / {self.__ar}"}}
    
    def get_days_sales_in_receivables_value(self):
        """return days sales in receivables value"""
        return {"value": self.__ar / self.__sales * 365}
    
    def get_days_sales_in_receivables_fourmula(self):
        """return days sales in receivables formula"""
        return {"formula": {"rule": "AR / Sales * 365",
                            "numbers": f"{self.__ar} / {self.__sales} * 365"}}
    
    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": self.__cogs / self.__ap}
    
    def get_payables_turnover_fourmula(self):
        """return payables turnover formula"""
        return {"formula": {"rule": "COGS / AP",
                            "numbers": f"{self.__cogs} / {self.__ap}"}}


class Profitability(AssetsTO, Leveraging, Lequidity):
    
    __ni = None
    __sales = None
    __intrest = None
    __ebit = None
    __ta = None
    __roe = None
    __roi = None
    __tax = None
    __dividansRatio = None
    
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    @property
    def date(self, year):
        self.__ni = self.__data['Financial Statements']['Income Statements'][year]['Net Income']
        self.__sales = self.__data['Financial Statements']['Income Statements'][year]['Sales']
        self.__ta = self.__data['Financial Statements']['Balance Sheets'][year]['Total Assets']
        self.__te = self.__data['Financial Statements']['Balance Sheets'][year]['Total Equity']
        self.__ebit = self.__data['Financial Statements']['Income Statements'][year]['EBIT']
        self.__intrest = self.__data['Financial Statements']['Income Statements'][year]['Interest Expense']
        self.__tax = self.__data['Financial Statements']['Income Statements'][year]['Taxes']
        self.__dividansRatio = self.__data['Financial Statements']['Income Statements'][year]['Dividans Ratio']
        if self.__dividansRatio == None or self.__dividansRatio == 0:
            self.__dividansRatio = self.__data['Financial Statements']['Income Statements'][year]['Dividans Ratio'] / self.__data['Financial Statements']['Income Statements'][year]['Net Income']
        
    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": self.__ni / self.__sales}
    
    def get_net_profit_margin_fourmula(self):
        """return net profit margin formula"""    
        return {"formula": {"rule": "NI / Sales",
                            "numbers": f"{self.__ni} / {self.__sales}"}}
    
    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": self.__ni / self.__ta}
    
    def get_return_on_assets_fourmula(self):
        """return return on assets formula"""
        return {"formula": {"rule": "NI / TA",
                            "numbers": f"{self.__ni} / {self.__ta}",
                            "rule": "TOTA * PM",
                            "numbers": f"{self.__ta} * {self.get_net_profit_margin_value()['value']}"}}

    def get_return_on_equity_value(self):
        """return return on equity value"""
        return {"value": self.__ni / self.__te}
    
    def get_return_on_equity_fourmula(self):
        """return return on equity formula"""
        return {"formula": {"rule": "NI / TE",
                            "numbers": f"{self.__ni} / {self.__te}",
                            "rule": "ROA * EM",
                            "numbers": f"{self.get_return_on_assets_value()['value']} * {self.get_equity_multiplier_value()['value']}"}}
    
    def get_roi_value(self):
        """return ROI value"""
        self.__roi = self.__ebit / self.__ta
        return {"value": self.__ebit / self.__ta}
    
    def get_roi_fourmula(self):
        """return ROI formula"""
        return {"formula": {"rule": "EBIT / TA",
                            "numbers": f"{self.__ebit} / {self.__ta}"}}
    
    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {"value": (self.get_roi_value()['value'] - self.__intrest) * self.get_debt_equity_ratio_value()['value']}
    
    def get_return_trade_on_equity_fourmula(self):
        """return return trade on equity formula"""
        return {"formula": {"rule": "(ROI - IE) * DER",
                            "numbers": f"({self.get_roi_value()['value']} - {self.__intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}
    
    def get_ROE_using_EOV(self):
        """return ROE using EOV"""
        self.get_roi_value()
        return {"value": (1 - self.__tax) * self.__roi + (self.__roi - self.__intrest) * self.get_debt_equity_ratio_value()['value']}
    
    def get_ROE_using_EOV_fourmula(self):
        """return ROE using EOV formula"""
        return {"formula": {"rule": "(1 - T) * ROI + (ROI - IE) * DER",
                            "numbers": f"(1 - {self.__tax}) * {self.__roi} + ({self.__roi} - {self.__intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}
    
    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": self.get_return_on_assets_value()['value'] * (1 - self.__dividansRatio)}


class MarketValue(Profitability):
    
    __number_of_shares = None
    __market_price = None
    __eps = None
    __book_value = None
    __equity = None
    
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    @property
    def date(self, year):
        self.__number_of_shares = self.__data['Financial Statements']['Income Statements'][year]['Number of Shares']
        self.__market_price = self.__data['Financial Statements']['Income Statements'][year]['Market Price']
        self.__eps = self.__data['Financial Statements']['Income Statements'][year]['EPS']
        self.__equity = self.__data['Financial Statements']['Balance Sheets'][year]['Total Equity']
        self.__book_value = self.__equity / self.__number_of_shares

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": self.__market_price / self.__eps}
    
    def get_pe_ratio_fourmula(self):
        """return PE ratio formula"""
        return {"formula": {"rule": "Market Price / EPS",
                            "numbers": f"{self.__market_price} / {self.__eps}"}}
    
    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": self.__market_price / self.__book_value}
    
    def get_mb_ratio_fourmula(self):
        """return PB ratio formula"""
        return {"formula": {"rule": "Market Price / Book Value",
                            "numbers": f"{self.__market_price} / {self.__book_value}"}}
    
    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": math.sqrt(1.5 * 15 * self.__book_value * self.__eps)}

class Engine(Lequidity, Leveraging, AssetsTO, Profitability):
    """engine class"""
    __data = None
    def __init__(self) -> None:
        self.__data = json.load(open('company.json'))
    
    def get_dates(self):
        """return dates"""
        return list(self.__data['Financial Statements']['Balance Sheets'])
    
    def set_date(self, year):
        self.date(year)
        