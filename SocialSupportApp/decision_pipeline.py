import joblib
from features_for_prediction import extract_features

def load_model():
    return joblib.load("eligibility_model.pkl")

def make_decision(input_data):
    model = load_model()
    features = extract_features(input_data)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()

    return {
        "decision": "Approve" if prediction == 1 else "Soft Decline",
        "confidence": round(probability, 3)
    }