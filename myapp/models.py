from django.db import models
import json
import math


# Create your models here.
class Lequidity():
    """lequidity class"""

    def get_current_ratio_value(self):
        """return current ratio value"""
        return {
            "value": (
                self._cash +
                self._account_recivables +
                self._inventory) /
            self._totall_current_liabilty}

    def get_current_ratio_fourmula(self):
        """return current ratio formula"""
        numbers = f"({self._cash} + {self._account_recivables}"
        numbers += f" + {self._inventory}) / {self._totall_current_liabilty}"
        return {
            "formula": {
                "rule": "cash + AR + INV / CL",
                "numbers": f"{numbers}"}}

    def get_quick_ratio_value(self):
        """return quick ratio value"""
        return {
            "value": (
                self._cash +
                self._account_recivables) /
            self._totall_current_liabilty}

    def get_quick_ratio_fourmula(self):
        """return quick ratio formula"""
        numbers = f"({self._cash}"
        numbers += f" + {self._account_recivables}) / {self._totall_current_liabilty}"
        return {
            "formula": {
                "rule": "cash + AR / CL",
                "numbers": f"{numbers}"}}

    def get_cash_ratio_value(self):
        """return cash ratio value"""
        return {"value": self._cash / self._totall_current_liabilty}

    def get_cash_ratio_fourmula(self):
        """return cash ratio formula"""
        return {
            "formula": {
                "rule": "cash / CL",
                "numbers": f"{self._cash} / {self._totall_current_liabilty}"}}


class Leveraging():
    """leverage class"""

    def get_debt_ratio_value(self):
        """return debt ratio value"""
        return {"value": self._totall_debt / self._totall_assets}

    def get_debt_ratio_fourmula(self):
        """return debt ratio formula"""
        return {
            "formula": {
                "rule": "TD / TA",
                "numbers": f"{self._totall_debt} / {self._totall_assets}"}}

    def get_debt_equity_ratio_value(self):
        """return debt equity ratio value"""
        return {"value": self._totall_debt / self._totall_equity}

    def get_debt_equity_ratio_fourmula(self):
        """return debt equity ratio formula"""
        return {
            "formula": {
                "rule": "TD / TE",
                "numbers": f"{self._totall_debt} / {self._totall_equity}"}}

    def get_equity_multiplier_value(self):
        """return equity multiplier value"""
        return {"value": self._totall_assets / self._totall_equity}

    def get_equity_multiplier_fourmula(self):
        """return equity multiplier formula"""
        return {
            "formula": {
                "rule": "TA / TE",
                "numbers": f"{self._totall_assets} / {self._totall_equity}"}}

    def get_times_interest_earned_value(self):
        """return times interest earned value"""
        return {"value": self._EBIT / self._intrest}

    def get_times_interest_earned_fourmula(self):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self._EBIT} / {self._intrest}"}}

    def get_ebitda_coverage_value(self):
        """return EBITDA coverage value"""
        return {"value": self._EBITDA / self._intrest}

    def get_ebitda_coverage_fourmula(self):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self._EBITDA} / {self._intrest}"}}


class AssetsTO():
    """assets turn over class"""

    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": self._sales / self._totall_assets}

    def get_total_assets_turnover_fourmula(self):
        """return total assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / TA",
                "numbers": f"{self._sales} / {self._totall_assets}"}}

    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": self._sales / self._totall_fixed_assets}

    def get_fixed_assets_turnover_fourmula(self):
        """return fixed assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / FA",
                "numbers": f"{self._sales} / {self._totall_fixed_assets}"}}

    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": self._sales / self._totall_current_assets}

    def get_current_assets_turnover_fourmula(self):
        """return current assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / CA",
                "numbers": f"{self._sales} / {self._totall_current_assets}"}}

    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": self._cogs / self._inventory}

    def get_inventory_turnover_fourmula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self._cogs} / {self._inventory}"}}

    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": self._inventory / self._cogs * 365}

    def get_days_sales_in_inventory_fourmula(self):
        """return days sales in inventory formula"""
        return {
            "formula": {
                "rule": "INV / COGS * 365",
                "numbers": f"{self._inventory} / {self._cogs} * 365"}}

    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": self._sales / self._account_recivables}

    def get_receivables_turnover_fourmula(self):
        """return receivables turnover formula"""
        return {
            "formula": {
                "rule": "Sales / AR",
                "numbers": f"{self._sales} / {self._account_recivables}"}}

    def get_days_sales_in_receivables_value(self):
        """return days sales in receivables value"""
        return {"value": self._account_recivables / self._sales * 365}

    def get_days_sales_in_receivables_fourmula(self):
        """return days sales in receivables formula"""
        numbers = f"{self._account_recivables} / {self._sales} * 365"
        return {
            "formula": {
                "rule": "AR / Sales * 365",
                "numbers": f"{numbers}"}}

    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": self._cogs / self._account_payable}

    def get_payables_turnover_fourmula(self):
        """return payables turnover formula"""
        return {
            "formula": {
                "rule": "COGS / AP",
                "numbers": f"{self._cogs} / {self._account_payable}"}}


class Profitability(Leveraging):

    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": self._net_income / self._sales}

    def get_net_profit_margin_fourmula(self):
        """return net profit margin formula"""
        return {"formula": {"rule": "NI / Sales",
                            "numbers": f"{self._net_income} / {self._sales}"}}

    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": self._net_income / self._totall_assets}

    def get_return_on_assets_fourmula(self):
        """return return on assets formula"""
        return {
            "formula": {
                "rule": "NI / TA",
                "numbers": f"{self._net_income} / {self._totall_assets}",
                "rule": "TOTA * PM",
                "numbers": f"{self._totall_assets} * {self.get_net_profit_margin_value()['value']}"}}

    def get_return_on_equity_value(self):
        """return return on equity value"""
        return {"value": self._net_income / self._totall_equity}

    def get_return_on_equity_fourmula(self):
        """return return on equity formula"""
        return {
            "formula": {
                "rule": "NI / TE",
                "numbers": f"{self._net_income} / {self._totall_equity}",
                "rule": "ROA * EM",
                "numbers": f"{self.get_return_on_assets_value()['value']} * {self.get_equity_multiplier_value()['value']}"}}

    def get_roi_value(self):
        """return ROI value"""
        self._roi = self._ebit / self._totall_assets
        return {"value": self._ebit / self._totall_assets}

    def get_roi_fourmula(self):
        """return ROI formula"""
        return {
            "formula": {
                "rule": "EBIT / TA",
                "numbers": f"{self._ebit} / {self._totall_assets}"}}

    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {
            "value": (
                self.get_roi_value()['value'] -
                self._intrest) *
            self.get_debt_equity_ratio_value()['value']}

    def get_return_trade_on_equity_fourmula(self):
        """return return trade on equity formula"""
        return {
            "formula": {
                "rule": "(ROI - IE) * DER",
                "numbers": f"({self.get_roi_value()['value']} - {self._intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_ROE_using_EOV_value(self):
        """return ROE using EOV"""
        self.get_roi_value()
        return {"value": (1 -
                          self._tax_rate) *
                self._roi +
                (self._roi -
                 self._intrest) *
                self.get_debt_equity_ratio_value()['value']}

    def get_ROE_using_EOV_fourmula(self):
        """return ROE using EOV formula"""
        return {
            "formula": {
                "rule": "(1 - T) * ROI + (ROI - IE) * DER",
                "numbers": f"(1 - {self._tax_rate}) * {self._roi} + ({self._roi} - {self._intrest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": self.get_return_on_assets_value(
        )['value'] * (1 - self._dividansRatio)}


class MarketValue():

    def get_eps_value(self):
        """return EPS value"""
        return {"value": self._eps}

    def get_eps_fourmula(self):
        """return EPS formula"""
        return {"formula": {"rule": "NI / Number of Shares",
                            "numbers": f"{self._net_income} / {self._number_of_shares}"}}

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": self._market_price / self._eps}

    def get_pe_ratio_fourmula(self):
        """return PE ratio formula"""
        return {"formula": {"rule": "Market Price / EPS",
                            "numbers": f"{self._market_price} / {self._eps}"}}

    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": self._market_price / self._book_value}

    def get_mb_ratio_fourmula(self):
        """return PB ratio formula"""
        return {"formula": {"rule": "Market Price / Book Value",
                            "numbers": f"{self._market_price} / {self._book_value}"}}

    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": math.sqrt(1.5 * 15 * self._book_value * self._eps)}


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
        self._equity = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Equity']
        self._book_value = self._equity / self._number_of_shares
        self._net_income = self._data['Financial Statements'][
            'Income Statements'][year]['Net Income']
        self._sales = self._data['Financial Statements'][
            'Income Statements'][year]['Sales']
        self._totall_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._totall_equity = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Equity']
        self._ebit = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._intrest = self._data['Financial Statements'][
            'Income Statements'][year]['Interest Expense']
        self._tax_rate = self._data['Financial Statements'][
            'Income Statements'][year]['Tax Rate']
        self._dividansRatio = self._data['Financial Statements'][
            'Income Statements'][year]['Dividans Ratio']
        self._totall_fixed_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Fixed Assets']
        self._totall_current_assets = self._data['Financial Statements'][
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
        self._totall_current_liabilty = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Current Liabilities']
        self._totall_debt = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Debt']
        self._totall_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._EBIT = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._EBITDA = self._data['Financial Statements'][
            'Income Statements'][year]['EBITDA']
        self._eps = self._net_income / self._number_of_shares
        if self._dividansRatio is None or self._dividansRatio == 0:
            self._dividansRatio = self._data['Financial Statements'][
                'Income Statements'][year]['Dividans Ratio'] / \
                self._data['Financial Statements']['Income Statements'][year]['Net Income']
