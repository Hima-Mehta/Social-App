# features_for_prediction.py
import pandas as pd

def extract_features(inputs: dict) -> pd.DataFrame:
    """
    Takes a dictionary like:
    {
        "monthly_income": 7200,
        "employment_years": 2,
        "family_size": 4,
        "total_assets": 100000,
        "total_liabilities": 15000,
        "credit_score": 670
    }

    Returns a DataFrame of processed features for ML prediction.
    """
    features = pd.DataFrame([{
        "monthly_income": inputs["monthly_income"],
        "employment_years": inputs["employment_years"],
        "family_size": inputs["family_size"],
        "debt_to_asset_ratio": inputs["total_liabilities"] / max(inputs["total_assets"], 1),
        "credit_score": inputs["credit_score"]
    }])
    return features