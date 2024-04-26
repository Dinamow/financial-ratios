# Financial Ratios Calculator

**Repository Name:** financial-ratios

**Technology Used:** Django

## Purpose

This project aims to automate the calculation of financial ratios including Liquidity, Leverage, Assets Turnover, Profitability, and Market Value based on provided financial information.

## Features

1. **Comparison Between Two Years:**
   - Users can compare financial ratios between two years.
   - Example Format:

     ```json
     {
         "ratios": ["current ratio", "quick ratio"],
         "2023": {
             "current ratio": 1.5,
             "quick ratio": 1.5
         },
         "2024": {
             "current ratio": 1.5,
             "quick ratio": 1.5
         }
     }
     ```

2. **Detailed View for One Year:**
   - Detailed breakdown of ratios for a single year.
   - Example Format:

     ```json
     "2023": [
         {
             "type": "current ratio",
             "value": 1.5,
             "formula": "current assets / current liabilities",
             "number": "1.5 / 1.0"
         },
         {
             "type": "quick ratio",
             "value": 1.0,
             "formula": "current assets - INV / current liabilities",
             "number": "1.5 / 1.0"
         }
     ]
     ```

3. **Ratio Details View:**
   - Detailed view of a specific ratio for both years.
   - Example Format:

     ```json
     {
         "ratio": "current ratio",
         "formula": "current assets / current liabilities",
         "componotes": ["current assets", "current liabilities"],
         "2023": {
             "value": 1.5,
             "current assets": 1.5,
             "current liabilities": 1.0,
             "numbers": "1.5 / 1.0"
         },
         "2024": {
             "value": 1.5,
             "current assets": 1.5,
             "current liabilities": 1.0,
             "numbers": "1.5 / 1.0"
         }
     }
     ```

4. **Automated Calculation:**
   - Users can provide financial values with company and year, and the system will calculate all the ratios automatically.
