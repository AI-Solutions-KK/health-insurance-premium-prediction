import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    page_icon="🩺",
    layout="wide"
)

# ==================================================
# API CONFIG
# ==================================================
API_URL = os.getenv("MODEL_API_URL")
API_KEY = os.getenv("MODEL_API_KEY")

if not API_URL or not API_KEY:
    st.error("❌ API configuration missing.")
    st.stop()

API_URL = API_URL.rstrip("/") + "/predict"

HEADERS = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": API_KEY
}


# ==================================================
# CUSTOM STYLES (UI ONLY)
# ==================================================
st.markdown("""
<style>
.main { background-color: #0e1117; }

h1, h2, h3, h4 {
    color: #ffffff;
}

label {
    color: #c9d1d9 !important;
    font-weight: 500;
}

.card {
    background: #161b22;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #30363d;
    margin-bottom: 20px;
}

.badge {
    background: linear-gradient(90deg, #7ee787, #2ea043);
    padding: 10px 18px;
    border-radius: 30px;
    font-size: 20px;
    font-weight: 700;
    color: #0e1117;
    display: inline-block;
}

.stButton>button {
    width: 100%;
    height: 3.3em;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
    background: linear-gradient(90deg, #238636, #2ea043);
    color: white;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #2ea043, #238636);
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.markdown("""
<div class="card">
<h1>🩺 Health Insurance Premium Predictor</h1>
<p style="color:#9da7b1;">
AI-powered premium estimation • Secure • Cloud Deployed
</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# MAIN LAYOUT - TWO COLUMNS
# ==================================================
col_left, col_right = st.columns(2)

# LEFT COLUMN - BASIC DETAILS & HEALTH
with col_left:
    st.markdown("<div class='card'><h3>👤 Personal Details</h3></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        age = st.number_input("🎂 Age", 18, 100, 30)
        dependants = st.number_input("👨‍👩‍👧 Dependants", 0, 10, 0)
        income = st.number_input("💰 Annual Income (Lakhs)", 0, 200, 10)
        genetical_risk = st.slider("🧬 Genetic Risk Index", 0, 5, 1)

    with c2:
        gender = st.selectbox("⚧ Gender", ["Male", "Female"])
        marital_status = st.selectbox("💍 Marital Status", ["Married", "Unmarried"])
        employment_status = st.selectbox("🏢 Employment", ["Salaried", "Self-Employed"])
        bmi = st.selectbox("⚖️ BMI Category", ["Normal", "Overweight", "Obesity", "Underweight"])

# RIGHT COLUMN - POLICY & PREDICTION
with col_right:
    st.markdown("<div class='card'><h3>🩺 Health & Policy Details</h3></div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        smoking = st.selectbox("🚬 Smoking Status", ["No", "Occasional", "Regular"])
        medical_history = st.selectbox(
            "📋 Pre-Existing Conditions",
            [
                "None",
                "Diabetes",
                "High blood pressure",
                "Heart disease",
                "Diabetes & High blood pressure",
                "Diabetes & Heart disease",
                "Thyroid",
            ],
        )

    with c4:
        insurance_plan = st.selectbox("📄 Insurance Plan", ["Bronze", "Silver", "Gold"])
        region = st.selectbox("🌍 Region", ["Northwest", "Southeast", "Southwest"])

    # ==================================================
    # PREDICTION BUTTON & RESULT
    # ==================================================
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔮 Predict Premium"):
        payload = {
            "age": age,
            "dependants": dependants,
            "income": income,
            "genetical_risk": genetical_risk,
            "insurance_plan": insurance_plan,
            "gender": gender,
            "marital_status": marital_status,
            "employment_status": employment_status,
            "bmi": bmi,
            "smoking": smoking,
            "region": region,
            "medical_history": medical_history,
        }

        with st.spinner("⏳ Calculating premium..."):
            try:
                response = requests.post(API_URL,json=payload,headers=HEADERS,timeout=15)

                if response.status_code == 200:
                    premium = response.json()["predicted_premium"]

                    st.markdown(
                        f"""
                        <div class="card" style="text-align:center;">
                            <h3>💸 Estimated Annual Premium</h3>
                            <div class="badge">₹ {premium:,}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                else:
                    st.error(f"❌ API Error ({response.status_code})")

            except requests.exceptions.RequestException:
                st.error("❌ Unable to connect to Model API")

# ==================================================
# FOOTER
# ==================================================
st.markdown("""
<hr style="border:0.5px solid #30363d;">
<p style="text-align:center; color:#8b949e;">
Built with ❤️ using <b>Streamlit</b> • Model served via <b>Azure App Service (FastAPI)</b>
</p>
""", unsafe_allow_html=True)