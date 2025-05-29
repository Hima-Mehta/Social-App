import re

def extract_income(bank_text):
    matches = re.findall(r'Income\s?:?\s?AED\s?([\d,]+)', bank_text)
    if matches:
        return float(matches[0].replace(',', ''))
    return 0

def extract_employment_years(resume_text):
    # crude rule-based estimate: count years in text
    years = re.findall(r'\b20[0-2][0-9]\b', resume_text)
    if len(years) >= 2:
        return abs(int(years[-1]) - int(years[0]))
    return 1

def extract_family_size(id_text):
    return 4 if "Father" in id_text and "Mother" in id_text else 1

def extract_assets_liabilities(excel_df):
    total_assets = excel_df["Assets"].sum()
    total_liabilities = excel_df["Liabilities"].sum()
    return total_assets, total_liabilities
