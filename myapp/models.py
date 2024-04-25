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
    number_of_shares = models.FloatField(
        verbose_name="Number of Shares", default=0.0)
    market_price = models.FloatField(verbose_name="Market Price", default=0.0)
    net_income = models.FloatField(verbose_name="Net Income", default=0.0)
    sales = models.FloatField(verbose_name="Sales", default=0.0)
    total_assets = models.FloatField(verbose_name="Total Assets", default=0.0)
    total_equity = models.FloatField(verbose_name="Total Equity", default=0.0)
    ebit = models.FloatField(verbose_name="EBIT", default=0.0)
    interest = models.FloatField(verbose_name="Interest Expense", default=0.0)
    tax_rate = models.FloatField(verbose_name="Tax Rate", default=0.0)
    dividends = models.FloatField(verbose_name="Dividends", default=0.0)
    total_fixed_assets = models.FloatField(
        verbose_name="Fixed Assets", default=0.0)
    total_current_assets = models.FloatField(
        verbose_name="Total Current Assets", default=0.0)
    cogs = models.FloatField(
        verbose_name="Cost of Revenue, Total",
        default=0.0)
    inventory = models.FloatField(verbose_name="Total Inventory", default=0.0)
    account_receivables = models.FloatField(
        verbose_name="Total Receivables, Net", default=0.0)
    account_payable = models.FloatField(
        verbose_name="Accounts Payable", default=0.0)
    cash = models.FloatField(verbose_name="Cash & Equivalents", default=0.0)
    total_current_liability = models.FloatField(
        verbose_name="Total Current Liabilities", default=0.0)
    total_debt = models.FloatField(verbose_name="Total Debt", default=0.0)
    ebitda = models.FloatField(verbose_name="EBITDA", default=0.0)
    dividansRatio = models.FloatField(
        verbose_name="Dividans Ratio",
        default=0.0,
        editable=False)
    book_value = models.FloatField(verbose_name="Book Value", default=0.0,
                                   editable=False)
    eps = models.FloatField(verbose_name="EPS", default=0.0,
                            editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        for coloumn in self._meta.fields:
            n = coloumn.name
            v = getattr(self, n)
            if n != 'id' and n != 'company' and n != 'date':
                if n != 'dividansRatio' and n != 'book_value' and n != 'eps':
                    setattr(self, n, float(v))

        self.dividansRatio = self.get_dividans_ratio()
        self.book_value = self.get_book_value()
        self.eps = self.get_eps()
        super().save(*args, **kwargs)

    def get_dividans_ratio(self):
        return round(
            self.dividends / self.net_income,
            2) if self.net_income != 0 else 0.0

    def get_book_value(self):
        return round(self.total_equity / self.number_of_shares,
                     2) if self.number_of_shares != 0 else 0.0

    def get_eps(self):
        return round(self.net_income / self.number_of_shares,
                     2) if self.number_of_shares != 0 else 0.0

    def __str__(self) -> str:
        return self.company.name + ' - ' + self.date.date


class Lequidity():
    """lequidity class"""

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
        self.__cash = ratios_obj.cash
        self.__account_receivables = ratios_obj.account_receivables
        self.__inventory = ratios_obj.inventory
        self.__total_current_liability = ratios_obj.total_current_liability

    def get_current_ratio_value(self):
        """return current ratio value"""
        return {
            "value": round((
                self.__cash +
                self.__account_receivables +
                self.__inventory) /
                self.__total_current_liability, 2)}

    def get_current_ratio_formula(self):
        """return current ratio formula"""
        numbers = f"({self.__cash} + {self.__account_receivables}"
        numbers += f" + {self.__inventory}) / {self.__total_current_liability}"
        return {
            "formula": {
                "rule": "cash + AR + INV / CL",
                "numbers": f"{numbers}"}}

    def get_quick_ratio_value(self):
        """return quick ratio value"""
        return {
            "value": round(
                (self.__cash +
                 self.__account_receivables) /
                self.__total_current_liability,
                2)}

    def get_quick_ratio_formula(self):
        """return quick ratio formula"""
        numbers = f"({self.__cash}"
        numbers += f" + {self.__account_receivables}) / "
        numbers += f"{self.__total_current_liability}"
        return {
            "formula": {
                "rule": "cash + AR / CL",
                "numbers": f"{numbers}"}}

    def get_cash_ratio_value(self):
        """return cash ratio value"""
        return {
            "value": round(
                self.__cash /
                self.__total_current_liability,
                2)}

    def get_cash_ratio_formula(self):
        """return cash ratio formula"""
        numbers = f"{self.__cash} / {self.__total_current_liability}"
        return {
            "formula": {
                "rule": "cash / CL",
                "numbers": f"{numbers}"}}


class Leveraging():
    """leverage class"""

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
        self.__total_debt = ratios_obj.total_debt
        self.__total_assets = ratios_obj.total_assets
        self.__total_equity = ratios_obj.total_equity
        self.__ebit = ratios_obj.ebit
        self.__interest = ratios_obj.interest
        self.__ebitda = ratios_obj.ebitda

    def get_debt_ratio_value(self):
        """return debt ratio value"""
        return {"value": round(self.__total_debt / self.__total_assets, 2)}

    def get_debt_ratio_formula(self):
        """return debt ratio formula"""
        return {
            "formula": {
                "rule": "TD / TA",
                "numbers": f"{self.__total_debt} / {self.__total_assets}"}}

    def get_debt_equity_ratio_value(self):
        """return debt equity ratio value"""
        return {"value": round(self.__total_debt / self.__total_equity, 2)}

    def get_debt_equity_ratio_formula(self):
        """return debt equity ratio formula"""
        return {
            "formula": {
                "rule": "TD / TE",
                "numbers": f"{self.__total_debt} / {self.__total_equity}"}}

    def get_equity_multiplier_value(self):
        """return equity multiplier value"""
        return {"value": round(self.__total_assets / self.__total_equity, 2)}

    def get_equity_multiplier_formula(self):
        """return equity multiplier formula"""
        return {
            "formula": {
                "rule": "TA / TE",
                "numbers": f"{self.__total_assets} / {self.__total_equity}"}}

    def get_times_interest_earned_value(self):
        """return times interest earned value"""
        return {"value": round(self.__ebit / self.__interest, 2)}

    def get_times_interest_earned_formula(self):
        """return times interest earned formula"""
        return {"formula": {"rule": "EBIT / IE",
                            "numbers": f"{self.__ebit} / {self.__interest}"}}

    def get_ebitda_coverage_value(self):
        """return EBITDA coverage value"""
        return {"value": round(self.__ebitda / self.__interest, 2)}

    def get_ebitda_coverage_formula(self):
        """return EBITDA coverage formula"""
        return {"formula": {"rule": "EBITDA / IE",
                            "numbers": f"{self.__ebitda} / {self.__interest}"}}


class AssetsTO():
    """assets turn over class"""

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
        self.__sales = ratios_obj.sales
        self.__total_assets = ratios_obj.total_assets
        self.__total_fixed_assets = ratios_obj.total_fixed_assets
        self.__total_current_assets = ratios_obj.total_current_assets
        self.__cogs = ratios_obj.cogs
        self.__inventory = ratios_obj.inventory
        self.__account_receivables = ratios_obj.account_receivables
        self.__account_payable = ratios_obj.account_payable

    def get_total_assets_turnover_value(self):
        """return total assets turnover value"""
        return {"value": round(self.__sales / self.__total_assets, 2)}

    def get_total_assets_turnover_formula(self):
        """return total assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / TA",
                "numbers": f"{self.__sales} / {self.__total_assets}"}}

    def get_fixed_assets_turnover_value(self):
        """return fixed assets turnover value"""
        return {"value": round(self.__sales / self.__total_fixed_assets, 2)}

    def get_fixed_assets_turnover_formula(self):
        """return fixed assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / FA",
                "numbers": f"{self.__sales} / {self.__total_fixed_assets}"}}

    def get_current_assets_turnover_value(self):
        """return current assets turnover value"""
        return {"value": round(self.__sales / self.__total_current_assets, 2)}

    def get_current_assets_turnover_formula(self):
        """return current assets turnover formula"""
        return {
            "formula": {
                "rule": "Sales / CA",
                "numbers": f"{self.__sales} / {self.__total_current_assets}"}}

    def get_inventory_turnover_value(self):
        """return inventory turnover value"""
        return {"value": round(self.__cogs / self.__inventory, 2)}

    def get_inventory_turnover_formula(self):
        """return inventory turnover formula"""
        return {"formula": {"rule": "COGS / INV",
                            "numbers": f"{self.__cogs} / {self.__inventory}"}}

    def get_days_sales_in_inventory_value(self):
        """return days sales in inventory value"""
        return {"value": round(self.__inventory / self.__cogs * 360, 2)}

    def get_days_sales_in_inventory_formula(self):
        """return days sales in inventory formula"""
        return {
            "formula": {
                "rule": "INV / COGS * 360",
                "numbers": f"{self.__inventory} / {self.__cogs} * 360"}}

    def get_receivables_turnover_value(self):
        """return receivables turnover value"""
        return {"value": round(self.__sales / self.__account_receivables, 2)}

    def get_receivables_turnover_formula(self):
        """return receivables turnover formula"""
        return {
            "formula": {
                "rule": "Sales / AR",
                "numbers": f"{self.__sales} / {self.__account_receivables}"}}

    def get_days_sales_outstanding_value(self):
        """return days sales in receivables value"""
        return {
            "value": round(
                self.__account_receivables /
                self.__sales *
                360,
                2)}

    def get_days_sales_outstanding_formula(self):
        """return days sales in receivables formula"""
        numbers = f"{self.__account_receivables} / {self.__sales} * 360"
        return {
            "formula": {
                "rule": "AR / Sales * 360",
                "numbers": f"{numbers}"}}

    def get_payables_turnover_value(self):
        """return payables turnover value"""
        return {"value": round(self.__cogs / self.__account_payable, 2)}

    def get_payables_turnover_formula(self):
        """return payables turnover formula"""
        return {
            "formula": {
                "rule": "COGS / AP",
                "numbers": f"{self.__cogs} / {self.__account_payable}"}}

    def get_paid_period_value(self):
        """return paid period value"""
        return {"value": round(self.__account_payable / self.__cogs * 360, 2)}

    def get_paid_period_formula(self):
        """return paid period formula"""
        return {
            "formula": {
                "rule": "AP / COGS * 360",
                "numbers": f"{self.__account_payable} / {self.__cogs} * 360"}}


class Profitability():

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
        self.__net_income = ratios_obj.net_income
        self.__total_debt = ratios_obj.total_debt
        self.__sales = ratios_obj.sales
        self.__total_assets = ratios_obj.total_assets
        self.__total_equity = ratios_obj.total_equity
        self.__ebit = ratios_obj.ebit
        self.__interest = ratios_obj.interest
        self.__tax_rate = ratios_obj.tax_rate
        self.__dividends_ratio = ratios_obj.dividansRatio
        self.__em = round(self.__total_assets / self.__total_equity, 2)
        self.__roi = round(self.__ebit / self.__total_assets, 2)
        self.__de = round(self.__total_debt / self.__total_equity, 2)

    def get_net_profit_margin_value(self):
        """return net profit margin value"""
        return {"value": round(self.__net_income / self.__sales, 2)}

    def get_net_profit_margin_formula(self):
        """return net profit margin formula"""
        return {
            "formula": {
                "rule": "NI / Sales",
                "numbers": f"{self.__net_income} / {self.__sales}"}}

    def get_return_on_assets_value(self):
        """return return on assets value"""
        return {"value": round(self.__net_income / self.__total_assets, 2)}

    def get_return_on_assets_formula(self):
        """return return on assets formula"""
        numbers = f"{self.__total_assets} * "
        numbers += f"{self.get_net_profit_margin_value()['value']}"
        return {
            "formula": {
                "rule": "NI / TA",
                "numbers": f"{self.__net_income} / {self.__total_assets}",
                "rule": "TOTA * PM",
                "numbers": f"{numbers}"}}

    def get_return_on_equity_value(self):
        """return return on equity value"""
        return {"value": round(self.__net_income / self.__total_equity, 2)}

    def get_return_on_equity_formula(self):
        """return return on equity formula"""
        numbers = f"{self.get_return_on_assets_value()['value']}"
        return {
            "formula": {
                "rule": "NI / TE",
                "numbers": f"{self.__net_income} / {self.__total_equity}",
                "rule": "ROA * EM",
                "numbers": f"{numbers} * {self.__em}"}}

    def get_return_on_investment_value(self):
        """return return on investment value"""

        return {"value": round(self.__ebit / self.__total_assets, 2)}

    def get_return_on_investment_formula(self):
        """return return on investment formula"""
        return {
            "formula": {
                "rule": "EBIT / TA",
                "numbers": f"{self.__ebit} / {self.__total_assets}"}}

    def get_return_trade_on_equity_value(self):
        """return return trade on equity value"""
        return {
            "value": round(
                (self.get_return_on_investment_value()['value'] -
                 self.__interest) *
                self.__de,
                2)}

    def get_return_trade_on_equity_formula(self):
        """return return trade on equity formula"""
        numbers = f"({self.get_return_on_investment_value()['value']}"
        numbers += f" - {self.__interest}) * {self.__de}"
        return {
            "formula": {
                "rule": "(ROI - IE) * DER",
                "numbers": f"{numbers}"}}

    def get_return_trade_on_equity_using_eva_value(self):
        """return return trade on equity using eva"""
        self.get_return_on_investment_value()
        return {"value": round((1 -
                                self.__tax_rate) *
                self.__roi +
                (self.__roi -
                 self.__interest) *
                self.__de, 2)}

    def get_return_trade_on_equity_using_eva_formula(self):
        """return return trade on equity using eva formula"""
        numbers = f"(1 - {self.__tax_rate}) * {self.__roi}"
        numbers += f" + ({self.__roi} - {self.__interest}) * {self.__de}"
        return {
            "formula": {
                "rule": "(1 - TR) * ROI + (ROI - IE) * DER",
                "numbers": f"{numbers}"}}

    def get_internal_growth_rate_value(self):
        """return internal growth rate value"""
        return {"value": round(self.get_return_on_assets_value(
        )['value'] * (1 - self.__dividends_ratio), 2)}

    def get_internal_growth_rate_formula(self):
        """return internal growth rate formula"""
        numbers = f"{self.get_return_on_assets_value()['value']} * "
        numbers += f"(1 - {self.__dividends_ratio})"
        return {
            "formula": {
                "rule": "ROA * (1 - DR)",
                "numbers": f"{numbers}"}}

    def get_sustainable_growth_rate_value(self):
        """return sustainable growth rate value"""
        return {"value": round(self.get_return_on_assets_value(
        )['value'] * (1 - self.__dividends_ratio), 2)}

    def get_sustainable_growth_rate_formula(self):
        """return sustainable growth rate formula"""
        numbers = f"{self.get_return_on_assets_value()['value']} * "
        numbers += f"(1 - {self.__dividends_ratio})"
        return {
            "formula": {
                "rule": "ROA * (1 - DR)",
                "numbers": f"{numbers}"}}


class MarketValue():

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
        self.__number_of_shares = ratios_obj.number_of_shares
        self.__market_price = ratios_obj.market_price
        self.__net_income = ratios_obj.net_income
        self.__book_value = ratios_obj.book_value
        self.__eps = ratios_obj.eps

    def get_eps_value(self):
        """return EPS value"""
        return {"value": self.__eps}

    def get_eps_formula(self):
        """return EPS formula"""
        return {
            "formula": {
                "rule": "NI / Number of Shares",
                "numbers": f"{self.__net_income} / {self.__number_of_shares}"}}

    def get_pe_ratio_value(self):
        """return PE ratio value"""
        return {"value": round(self.__market_price / self.__eps, 2)}

    def get_pe_ratio_formula(self):
        """return PE ratio formula"""
        return {
            "formula": {
                "rule": "Market Price / EPS",
                "numbers": f"{self.__market_price} / {self.__eps}"}}

    def get_mb_ratio_value(self):
        """return PB ratio value"""
        return {"value": round(self.__market_price / self.__book_value, 2)}

    def get_mb_ratio_formula(self):
        """return PB ratio formula"""
        return {
            "formula": {
                "rule": "Market Price / BV",
                "numbers": f"{self.__market_price} / {self.__book_value}"}}

    def get_fair_value_of_stock_value(self):
        """return fair value of stock value"""
        return {"value": sqrt(1.5 * 15 * self.__book_value * self.__eps)}

    def get_fair_value_of_stock_formula(self):
        """return fair value of stock formula"""
        numbers = f"sqrt(1.5 * 15 * {self.__book_value} * {self.__eps})"
        return {
            "formula": {
                "rule": "sqrt(1.5 * 15 * BV * EPS)",
                "numbers": f"{numbers}"}}


class Engine(Lequidity, Leveraging, AssetsTO, Profitability, MarketValue):
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
            'number of shares',
            'market price',
            'net income',
            'sales',
            'total assets',
            'total equity',
            'ebit',
            'interest',
            'tax rate',
            'dividansRatio',
            'total fixed assets',
            'total current assets',
            'cogs',
            'inventory',
            'account receivables',
            'account payable',
            'cash',
            'total current liability',
            'total debt',
            'ebitda',
            'book value',
            'eps'
        ]
        self.__AVOID = [
            'book value',
            'eps',
            'dividansRatio'
        ]

    def get_dates(self):
        """return dates"""
        companies = Company.objects.all()
        data = []

        for company in companies:
            company_data = {
                'company': company.name,
                'Dates': list(
                    Ratios.objects.filter(
                        company=company).values_list(
                        'date__date',
                        flat=True).distinct())}
            data.append(company_data)
        return data

    def date(self, year, company):
        year_obj = Dates.objects.filter(date=year).first()
        company_obj = Company.objects.filter(name=company).first()
        if not year_obj or not company_obj:
            return None
        Lequidity.date(self, year, company)
        Leveraging.date(self, year, company)
        AssetsTO.date(self, year, company)
        Profitability.date(self, year, company)
        MarketValue.date(self, year, company)

    def get_raw_data(self, years, company):
        """return raw data (which is used to get ratios)"""
        raw_data = {}
        for year in years:
            year_obj = Dates.objects.filter(date=year).first()
            company_obj = Company.objects.filter(name=company).first()
            if not year_obj or not company_obj:
                return None
            ratios_obj = Ratios.objects.get(date=year_obj, company=company_obj)
            raw_data[year] = { ratio: getattr(ratios_obj, ratio.replace(' ', '_')) for ratio in self.__RAWDATA}
        return raw_data

    def get_date_ratios(self, year, company):
        """return date ratios"""
        self.date(year, company)

        ratios_info = {}
        for ratios in self.__RATIOSLIST.values():
            for ratio in ratios:
                ratio_data = {
                    'value': getattr(
                        self,
                        f"get_{ratio.lower().replace(' ', '_')}_value")
                    ()['value'],
                    'formula': getattr(
                        self,
                        f"get_{ratio.lower().replace(' ', '_')}_formula")
                    ()['formula']}
                ratios_info[ratio] = ratio_data

        return ratios_info

    def get_components(self, formula):
        formula = str(formula).replace("sqrt", "")
        components = re.findall(r'\b[\w.]+\b', str(formula))
        return components

    def get_components_values(self, numbers):
        components_values = re.findall(r'\d+\.\d+|\d+', str(numbers))
        return components_values

    def check_ratio(self, ratio):
        for ratios in self.__RATIOSLIST.values():
            if ratio in ratios:
                return False
        return True

    def get_ratio(self, ratio, years, company):
        """return ratio"""
        if self.check_ratio(ratio):
            return {"error": "Invalid ratio",
                    "ratios": list(self.__RATIOSLIST.values())}
        formula = self.get_date_ratios(years[0], company)[ratio]['formula']
        components: str = self.get_components(formula['rule'])
        ratio_info = {
            'ratio': ratio,
            'formula': formula['rule'],
            'components': components,
        }
        for year in years:
            ratio_info[year] = {
                'value': self.get_date_ratios(
                    year, company)[ratio]['value'],
                'numbers': self.get_date_ratios(
                    year, company)[ratio]['formula']['numbers'], }
            year_components_values = self.get_components_values(
                ratio_info[year]['numbers'])
            components_with_values = dict(
                zip(components, year_components_values))
            ratio_info[year].update(components_with_values)
        return ratio_info
    
    def get_values(self):
        """return values"""
        values = []
        for i in self.__RATIOSLIST:
            values.extend(i)
        return values

    def get_type(self, type, years, company):
        """return type"""

        if type not in self.__RATIOSLIST.keys():
            return {"error": "Invalid type",
                    "types": self.get_values()}

        ratios = self.__RATIOSLIST[type]

        if not years:
            return {"error": "Please provide years"}

        type_ratios = {}
        if len(years) == 1:
            year = years[0]
            type_ratios[year] = []
            for ratio in ratios:
                ratio_info = {
                    'type': ratio, 'value': self.get_date_ratios(
                        year, company)[ratio]['value'],
                    'formula': self.get_date_ratios(
                        year, company)[ratio]['formula']['rule'],
                    'numbers': self.get_date_ratios(
                        year, company)[ratio]['formula']['numbers']}
                type_ratios[year].append(ratio_info)
        else:
            type_ratios = {
                'ratios': ratios,
            }
            for year in years:
                type_ratios[year] = {
                    ratio.replace(' ', '_'): self.get_date_ratios(
                        year, company)[ratio]['value'] for ratio in ratios}
        return type_ratios
    
    def save_ratios(self, data: dict):
        """takes data and save them into db"""
        year = data.get('year')
        company = data.get('company')
        date = Dates.objects.filter(date=year).first()
        company = Company.objects.filter(name=company).first()

        if date and company:
            if Ratios.objects.filter(date=date, company=company).exists():
                return {"error": "Data already exists"}
        if not date:
            date = Dates.objects.create(date=year)
        if not company:
            company = Company.objects.create(name=data.get('company'))
        tmp = {}
        for i in self.__RAWDATA:
            if i not in self.__AVOID:
                if i not in data.keys():
                    return {"error": f"Missing {i}"}
                tmp[i.replace(' ', '_')] = data.get(i)
        Ratios.objects.create(date=date, company=company, **tmp)
        return {"message": "Data saved successfully"}

    def get_raw(self):
        data = []
        for i in self.__RAWDATA:
            if i != 'eps' and i != 'book value' and i != 'dividansRatio':
                data.append(i)
        return {'data': data}
