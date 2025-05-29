import pandas as pd
from Utils.data_parsing import *
from .data_ingestion import ingest_file
import os

records = []
def create_data():
    # Loop through multiple applicant folders or documents
    for applicant_folder in os.listdir("data"):
        # Placeholder extraction
        bank_text = ""
        resume_text = ""
        id_text = ""
        income = 0
        employment = 0
        assets, liabilities = 0,0
        family_size = 0

        excel_df = pd.DataFrame()
        if os.path.exists(f"data/{applicant_folder}/bank.pdf"):
            bank_text = ingest_file(f"data/{applicant_folder}/bank.pdf")
        if os.path.exists(f"data/{applicant_folder}/resume.pdf"):
            resume_text = ingest_file(f"data/{applicant_folder}/resume.pdf")
        if os.path.exists(f"data/{applicant_folder}/id.jpeg"):
            id_text = ingest_file(f"data/{applicant_folder}/id.jpeg")
        if os.path.exists(f"data/{applicant_folder}/assets.xlsx"):
            excel_df = ingest_file(f"data/{applicant_folder}/assets.xlsx")

        if bank_text!= "":
            income = extract_income(bank_text)
        if resume_text!="":
            employment = extract_employment_years(resume_text)
        if id_text!="":
            family_size = extract_family_size(id_text)
        if not excel_df.empty:
            assets, liabilities = extract_assets_liabilities(excel_df)

        # Example target — this should ideally come from manual labels
        label = 1 if income > 5000 else 0

        records.append({
            "monthly_income": income,
            "employment_years": employment,
            "family_size": family_size,
            "debt_to_asset_ratio": liabilities / (assets or 1),
            "credit_score": 680,  # placeholder
            "label": label
        })

    # Save training data
    df = pd.DataFrame(records)
    df.to_csv("training/data/training_set.csv", index=False)