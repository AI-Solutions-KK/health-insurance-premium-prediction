import pandas as pd
import joblib
from pathlib import Path

# ---------- Load Artifacts ----------
BASE_DIR = Path(__file__).resolve().parent.parent

model_young = joblib.load(BASE_DIR / "artifacts" / "model_young.joblib")
model_rest = joblib.load(BASE_DIR / "artifacts" / "model_rest.joblib")
scaler_young = joblib.load(BASE_DIR / "artifacts" / "scaler_young.joblib")
scaler_rest = joblib.load(BASE_DIR / "artifacts" / "scaler_rest.joblib")


# ---------- Helpers ----------
def calculate_normalized_risk(medical_history: str) -> float:
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    diseases = medical_history.lower().split(" & ")
    total_score = sum(risk_scores.get(d, 0) for d in diseases)

    return total_score / 14


def handle_scaling(age: int, df: pd.DataFrame) -> pd.DataFrame:
    scaler_object = scaler_young if age <= 25 else scaler_rest

    cols_to_scale = scaler_object["cols_to_scale"]
    scaler = scaler_object["scaler"]

    df["income_level"] = 0
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop(columns=["income_level"], inplace=True)

    return df


def preprocess_input(data: dict) -> pd.DataFrame:
    columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
        'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast',
        'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight',
        'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    df = pd.DataFrame(0, columns=columns, index=[0])

    plan_map = {"Bronze": 1, "Silver": 2, "Gold": 3}

    df["age"] = data["age"]
    df["number_of_dependants"] = data["dependants"]
    df["income_lakhs"] = data["income"]
    df["genetical_risk"] = data["genetical_risk"]
    df["insurance_plan"] = plan_map.get(data["insurance_plan"], 1)

    if data["gender"] == "Male":
        df["gender_Male"] = 1

    if data["marital_status"] == "Unmarried":
        df["marital_status_Unmarried"] = 1

    if data["employment_status"] == "Salaried":
        df["employment_status_Salaried"] = 1
    elif data["employment_status"] == "Self-Employed":
        df["employment_status_Self-Employed"] = 1

    if data["bmi"] == "Obesity":
        df["bmi_category_Obesity"] = 1
    elif data["bmi"] == "Overweight":
        df["bmi_category_Overweight"] = 1
    elif data["bmi"] == "Underweight":
        df["bmi_category_Underweight"] = 1

    if data["smoking"] == "Occasional":
        df["smoking_status_Occasional"] = 1
    elif data["smoking"] == "Regular":
        df["smoking_status_Regular"] = 1

    if data["region"] == "Northwest":
        df["region_Northwest"] = 1
    elif data["region"] == "Southeast":
        df["region_Southeast"] = 1
    elif data["region"] == "Southwest":
        df["region_Southwest"] = 1

    df["normalized_risk_score"] = calculate_normalized_risk(data["medical_history"])
    df = handle_scaling(data["age"], df)

    return df


def predict_premium(data: dict) -> int:
    df = preprocess_input(data)

    model = model_young if data["age"] <= 25 else model_rest
    prediction = model.predict(df)

    return int(prediction[0])
