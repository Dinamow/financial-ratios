from django.db import models
import json
import math


# Create your models here.
class Liquidity():
    """liquidity class"""

    def get_current_ratio_value(self):
        """return current ratio value"""
        return {
            "value": (
                self._cash +
                self._account_receivables +
                self._inventory) /
            self._total_current_liability}

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
            "value": (
                self._cash +
                self._account_receivables) /
            self._total_current_liability}

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
        return {"value": self._cash / self._total_current_liability}

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
        return {"value": self._total_debt / self._total_assets}

    def get_debt_ratio_formula(self):
        """return debt ratio formula"""
        return {
            "formula": {
                "rule": "TD / TA",
                "numbers": f"{self._total_debt} / {self._total_assets}"}}

    def get_debt_equity_ratio_value(self):
        """return debt equity ratio value"""
        return {"value": self._total_debt / self._total_equity}

    def get_debt_equity_ratio_formula(self):
        """return debt equity ratio formula"""
        return {
            "formula": {
                "rule": "TD / TE",
                "numbers": f"{self._total_debt} / {self._total_equity}"}}

    def get_equity_multiplier_value(self):
        """return equity multiplier value"""
        return {"value": self._total_assets / self._total_equity}

    def get_equity_multiplier_formula(self):
        """return equity multiplier formula"""
        return {
            "formula": {
                "rule": "TA / TE",
                "numbers": f"{self._total_assets} / {self._total_equity}"}}

    def get_times_interest_earned_value(self):
        """return times interest earned value"""
        return {"value": self._EBIT / self._interest}

    def get_times_interest_earned_formula(self):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self._EBIT} / {self._interest}"}}

    def get_ebitda_coverage_value(self):
        """return EBITDA coverage value"""
        return {"value": self._EBITDA / self._interest}

    def get_ebitda_coverage_formula(self):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self._EBITDA} / {self._interest}"}}


class AssetsTO():
    """assets turn over class"""

    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": self._sales / self._total_assets}

    def get_total_assets_turnover_formula(self):
        """return total assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / TA",
                "numbers": f"{self._sales} / {self._total_assets}"}}

    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": self._sales / self._total_fixed_assets}

    def get_fixed_assets_turnover_formula(self):
        """return fixed assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / FA",
                "numbers": f"{self._sales} / {self._total_fixed_assets}"}}

    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": self._sales / self._total_current_assets}

    def get_current_assets_turnover_formula(self):
        """return current assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / CA",
                "numbers": f"{self._sales} / {self._total_current_assets}"}}

    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": self._cogs / self._inventory}

    def get_inventory_turnover_formula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self._cogs} / {self._inventory}"}}

    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": self._inventory / self._cogs * 365}

    def get_days_sales_in_inventory_formula(self):
        """return days sales in inventory formula"""
        return {
            "formula": {
                "rule": "INV / COGS * 365",
                "numbers": f"{self._inventory} / {self._cogs} * 365"}}

    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": self._sales / self._account_receivables}

    def get_receivables_turnover_formula(self):
        """return receivables turnover formula"""
        return {
            "formula": {
                "rule": "Sales / AR",
                "numbers": f"{self._sales} / {self._account_receivables}"}}

    def get_days_sales_in_receivables_value(self):
        """return days sales in receivables value"""
        return {"value": self._account_receivables / self._sales * 365}

    def get_days_sales_in_receivables_formula(self):
        """return days sales in receivables formula"""
        numbers = f"{self._account_receivables} / {self._sales} * 365"
        return {
            "formula": {
                "rule": "AR / Sales * 365",
                "numbers": f"{numbers}"}}

    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": self._cogs / self._account_payable}

    def get_payables_turnover_formula(self):
        """return payables turnover formula"""
        return {
            "formula": {
                "rule": "COGS / AP",
                "numbers": f"{self._cogs} / {self._account_payable}"}}


class Profitability(Leveraging):

    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": self._net_income / self._sales}

    def get_net_profit_margin_formula(self):
        """return net profit margin formula"""
        return {"formula": {"rule": "NI / Sales",
                            "numbers": f"{self._net_income} / {self._sales}"}}

    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": self._net_income / self._total_assets}

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
        return {"value": self._net_income / self._total_equity}

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
        return {"value": self._ebit / self._total_assets}

    def get_return_on_investment_formula(self):
        """return return on investment formula"""
        return {
            "formula": {
                "rule": "EBIT / TA",
                "numbers": f"{self._ebit} / {self._total_assets}"}}

    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {
            "value": (
                self.get_return_on_investment_value()['value'] -
                self._interest) *
            self.get_debt_equity_ratio_value()['value']}

    def get_return_trade_on_equity_formula(self):
        """return return trade on equity formula"""
        return {
            "formula": {
                "rule": "(ROI - IE) * DER",
                "numbers": f"({self.get_return_on_investment_value()['value']} - {self._interest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_return_trade_on_equity_using_EVA_value(self):
        """return return trade on equity using EVA"""
        self.get_return_on_investment_value()
        return {"value": (1 -
                          self._tax_rate) *
                self._roi +
                (self._roi -
                 self._interest) *
                self.get_debt_equity_ratio_value()['value']}

    def get_return_trade_on_equity_using_EVA_formula(self):
        """return return trade on equity using EVA formula"""
        return {
            "formula": {
                "rule": "(1 - T) * ROI + (ROI - IE) * DER",
                "numbers": f"(1 - {self._tax_rate}) * {self._roi} + ({self._roi} - {self._interest}) * {self.get_debt_equity_ratio_value()['value']}"}}

    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": self.get_return_on_assets_value(
        )['value'] * (1 - self._dividendsRatio)}

    def get_internal_growth_rate_formula(self):
        """return internal growth rate formula"""
        return {
            "formula": {
                "rule": "ROA * (1 - DR)",
                "numbers": f"{self.get_return_on_assets_value()['value']} * (1 - {self._dividendsRatio})"}}

    def get_sustainable_growth_rate_value(self):
        """return sustainable growth rate value"""
        return {"value": self.get_return_on_equity_value(
        )['value'] * (1 - (self._dividendsRatio))}

    def get_sustainable_growth_rate_formula(self):
        """return sustainable growth rate formula"""
        return {
            "formula": {
                "rule": "ROE * (1 - DR)",
                "numbers": f"{self.get_internal_growth_rate_value()['value']} * {self.get_return_on_equity_value()['value']}"}}

class MarketValue():

    def get_eps_value(self):
        """return EPS value"""
        return {"value": self._eps}

    def get_eps_formula(self):
        """return EPS formula"""
        return {"formula": {"rule": "NI / Number of Shares",
                            "numbers": f"{self._net_income} / {self._number_of_shares}"}}

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": self._market_price / self._eps}

    def get_pe_ratio_formula(self):
        """return PE ratio formula"""
        return {"formula": {"rule": "Market Price / EPS",
                            "numbers": f"{self._market_price} / {self._eps}"}}

    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": self._market_price / self._book_value}

    def get_mb_ratio_formula(self):
        """return PB ratio formula"""
        return {"formula": {"rule": "Market Price / Book Value",
                            "numbers": f"{self._market_price} / {self._book_value}"}}

    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": math.sqrt(1.5 * 15 * self._book_value * self._eps)}

    def get_fair_value_of_stock_formula(self):
        """return fair value of stock formula"""
        return {
            "formula": {
                "rule": "sqrt(1.5 * 15 * BV * EPS)",
                "numbers": f"sqrt(1.5 * 15 * {self._book_value} * {self._eps})"}}

class Engine(Liquidity, AssetsTO, Profitability, MarketValue):
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
        self._total_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._total_equity = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Equity']
        self._ebit = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._interest = self._data['Financial Statements'][
            'Income Statements'][year]['Interest Expense']
        self._tax_rate = self._data['Financial Statements'][
            'Income Statements'][year]['Tax Rate']
        self._dividendsRatio = self._data['Financial Statements'][
            'Income Statements'][year]['Dividends Ratio']
        self._total_fixed_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Fixed Assets']
        self._total_current_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Current Assets']
        self._cogs = self._data['Financial Statements'][
            'Income Statements'][year]['Cost of Revenue, Total']
        self._inventory = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Inventory']
        self._account_receivables = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Receivables, Net']
        self._account_payable = self._data['Financial Statements'][
            'Balance Sheets'][year]['Accounts Payable']
        self._cash = self._data['Financial Statements'][
            'Balance Sheets'][year]['Cash & Equivalents']
        self._total_current_liability = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Current Liabilities']
        self._total_debt = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Debt']
        self._total_assets = self._data['Financial Statements'][
            'Balance Sheets'][year]['Total Assets']
        self._EBIT = self._data['Financial Statements'][
            'Income Statements'][year]['EBIT']
        self._EBITDA = self._data['Financial Statements'][
            'Income Statements'][year]['EBITDA']
        self._eps = self._net_income / self._number_of_shares
        if self._dividendsRatio is None or self._dividendsRatio == 0:
            self._dividendsRatio = self._data['Financial Statements'][
                'Income Statements'][year]['Dividends Ratio'] / \
                self._data['Financial Statements']['Income Statements'][year]['Net Income']

    def get_date_ratios(self, year):
        """return date ratios"""
        self.date(year)
        return {
            "Current Ratio": {'value': self.get_current_ratio_value()['value'], 'formula': self.get_current_ratio_formula()['formula']},
            "Quick Ratio": {'value': self.get_quick_ratio_value()['value'], 'formula': self.get_quick_ratio_formula()['formula']},
            "Cash Ratio": {'value': self.get_cash_ratio_value()['value'], 'formula': self.get_cash_ratio_formula()['formula']},
            "Debt Ratio": {'value': self.get_debt_ratio_value()['value'], 'formula': self.get_debt_ratio_formula()['formula']},
            "Debt Equity Ratio": {'value': self.get_debt_equity_ratio_value()['value'], 'formula': self.get_debt_equity_ratio_formula()['formula']},
            "Equity Multiplier": {'value': self.get_equity_multiplier_value()['value'], 'formula': self.get_equity_multiplier_formula()['formula']},
            "Times Interest Earned": {'value': self.get_times_interest_earned_value()['value'], 'formula': self.get_times_interest_earned_formula()['formula']},
            "EBITDA Coverage": {'value': self.get_ebitda_coverage_value()['value'], 'formula': self.get_ebitda_coverage_formula()['formula']},
            "Total Assets Turnover": {'value': self.get_total_assets_turnover_value()['value'], 'formula': self.get_total_assets_turnover_formula()['formula']},
            "Fixed Assets Turnover": {'value': self.get_fixed_assets_turnover_value()['value'], 'formula': self.get_fixed_assets_turnover_formula()['formula']},
            "Current Assets Turnover": {'value': self.get_current_assets_turnover_value()['value'], 'formula': self.get_current_assets_turnover_formula()['formula']},
            "Inventory Turnover": {'value': self.get_inventory_turnover_value()['value'], 'formula': self.get_inventory_turnover_formula()['formula']},
            "Days Sales in Inventory": {'value': self.get_days_sales_in_inventory_value()['value'], 'formula': self.get_days_sales_in_inventory_formula()['formula']},
            "Receivables Turnover": {'value': self.get_receivables_turnover_value()['value'], 'formula': self.get_receivables_turnover_formula()['formula']},
            "Days Sales in Receivables": {'value': self.get_days_sales_in_receivables_value()['value'], 'formula': self.get_days_sales_in_receivables_formula()['formula']},
            "Collection Period": {'value': self.get_days_sales_in_receivables_value()['value'], 'formula': self.get_days_sales_in_receivables_formula()['formula']},
            "Payables Turnover": {'value': self.get_payables_turnover_value()['value'], 'formula': self.get_payables_turnover_formula()['formula']},
            "Paid Period": {'value': self.get_payables_turnover_value()['value'], 'formula': self.get_payables_turnover_formula()['formula']},
            "Net Profit Margin": {'value': self.get_net_profit_margin_value()['value'], 'formula': self.get_net_profit_margin_formula()['formula']},
            "Return on Assets": {'value': self.get_return_on_assets_value()['value'], 'formula': self.get_return_on_assets_formula()['formula']},
            "Return on Equity": {'value': self.get_return_on_equity_value()['value'], 'formula': self.get_return_on_equity_formula()['formula']},
            "Return on Investment": {'value': self.get_return_on_investment_value()['value'], 'formula': self.get_return_on_investment_formula()['formula']},
            "Return Trade on Equity": {'value': self.get_return_trade_on_equity_value()['value'], 'formula': self.get_return_trade_on_equity_formula()['formula']},
            "Return Trade on Equity using EVA": {'value': self.get_return_trade_on_equity_using_EVA_value()['value'], 'formula': self.get_return_trade_on_equity_using_EVA_formula()['formula']},
            "Internal Growth Rate": {'value': self.get_internal_growth_rate_value()['value'], 'formula': self.get_internal_growth_rate_formula()['formula']},
            "Substantial Growth Rate": {'value': self.get_sustainable_growth_rate_value()['value'], 'formula': self.get_sustainable_growth_rate_formula()['formula']},
            "EPS": {'value': self.get_eps_value()['value'], 'formula': self.get_eps_formula()['formula']},
            "PE Ratio": {'value': self.get_pe_ratio_value()['value'], 'formula': self.get_pe_ratio_formula()['formula']},
            "MB Ratio": {'value': self.get_mb_ratio_value()['value'], 'formula': self.get_mb_ratio_formula()['formula']},
            "Fair Value of Stock": {'value': self.get_fair_value_of_stock_value()['value'], 'formula': self.get_fair_value_of_stock_formula()['formula']}
    }

    def get_ratio(self, ratio, years):
        """return ratio"""
        return {year: self.get_date_ratios(year)[ratio] for year in years}

    def get_type(self, type, years):
        """return type"""
        if type.lower() in ['liquidity', 'liquidity ratios', 'liquidity_ratios', 'liquidityratios']:
            ratios = ['Current Ratio', 'Quick Ratio', 'Cash Ratio']
        elif type.lower() in ['leverage', 'leverage ratios', 'leverageratios', 'leverage_ratios']:
            ratios = ['Debt Ratio', 'Debt Equity Ratio', 'Equity Multiplier', 'Times Interest Earned', 'EBITDA Coverage']
        elif type.lower() in ['assets turnover', 'assets_turnover', 'assetsturnover', 'assets', 'asset ratios', 'asset_ratios', 'assetratios']:
            ratios = ['Total Assets Turnover', 'Fixed Assets Turnover', 'Current Assets Turnover', 'Inventory Turnover', 'Days Sales in Inventory', 'Receivables Turnover', 'Days Sales in Receivables', 'Collection Period', 'Payables Turnover', 'Paid Period']
        elif type.lower() == 'profitability':
            ratios = ['Net Profit Margin', 'Return on Assets', 'Return on Equity', 'Return on Investment', 'Return Trade on Equity', 'Return Trade on Equity using EVA', 'Internal Growth Rate', 'Substantial Growth Rate']
        elif type.lower() in ['market value', 'market_value', 'marketvalue', 'market', 'market ratios', 'marketratios', 'market_ratios']:
            ratios = ['EPS', 'PE Ratio', 'MB Ratio', 'Fair Value of Stock']

        return {year: {ratio: self.get_date_ratios(year)[ratio] for ratio in ratios} for year in years}

    def get_statements(self, years, statements):
        """return statements"""
        return {year: {statement: self._data['Financial Statements'][statement][year] for statement in statements} for year in years}