import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    df = pd.read_csv("training/data/training_set.csv")
    X = df.drop("label", axis=1)
    y = df["label"]
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model to disk
    joblib.dump(model, "eligibility_model.pkl")
    print("✅ Model saved as eligibility_model.pkl")

if __name__ == "__main__":
    train_model()