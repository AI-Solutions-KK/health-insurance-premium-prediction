# 🏥 Health Insurance Premium Prediction – Cloud Deployed

A production-ready **Machine Learning web application** that predicts **health insurance premiums** based on user profile details.  
The system is fully **cloud deployed**, with a clean separation between **UI** and **Model API**.

---
- REPO: For model Deployment: Main model Repo 

https://github.com/AI-Solutions-KK/health-insurance-premium-model-api.git


- REPO : UI-APP - Practical Model use case 

https://github.com/AI-Solutions-KK/health-insurance-premium-prediction-ui.git


- APP : Live Deployed App: Model Test 

https://health-insurance-premium-ui-gvhvh4esfqe9emb5.centralindia-01.azurewebsites.net/

---

## 🔗 Live Architecture (Cloud Only)

```
User (Browser)
   ↓
Streamlit UI (Azure App Service)
   ↓  REST API call
FastAPI Model API (Azure App Service)
   ↓
ML Models (Scikit-learn / XGBoost)
```

---

## ✨ Key Features

- 🎯 Predicts insurance premium instantly
- ☁️ Fully cloud-hosted (Azure App Service)
- 🧠 ML models served via FastAPI
- 🎨 Modern, responsive Streamlit UI
- 🔐 Environment-variable based API configuration
- 🚀 CI/CD enabled via GitHub Actions

---

## 🧠 Model Inputs

The prediction is based on the following parameters:

- Age  
- Gender  
- Marital Status  
- Number of Dependents  
- Annual Income  
- BMI Category  
- Smoking Status  
- Pre-existing Medical Conditions  
- Insurance Plan (Silver / Gold / Platinum)  
- Region  

---

## 🖥️ Frontend (UI)

- **Framework**: Streamlit  
- **Deployment**: Azure App Service (Linux, Python 3.10)
- **Responsibility**:
  - Collect user inputs
  - Call live Model API
  - Display predicted premium with clean UI

The UI does **not** load models or perform inference locally.

---

## ⚙️ Backend (Model API)

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Models**:
  - Scikit-learn regression models
  - XGBoost
  - Joblib-serialized artifacts
- **Endpoint**:
  ```
  POST /predict
  ```

Example request payload:
```json
{
  "age": 35,
  "gender": "Male",
  "dependents": 2,
  "income": 15,
  "insurance_plan": "Gold",
  "bmi": "Overweight",
  "smoking": "Occasional",
  "region": "Southwest",
  "medical_history": "Diabetes"
}
```

---

## 🔐 Configuration

The UI connects to the Model API using an environment variable:

```
MODEL_API_URL=https://<your-model-api>.azurewebsites.net
```

No secrets or URLs are hardcoded.

---

## 📦 Tech Stack

- Python 3.10  
- Streamlit  
- FastAPI  
- Scikit-learn  
- XGBoost  
- Pandas / NumPy  
- Joblib  
- Azure App Service  
- GitHub Actions (CI/CD)

---

## 📁 Project Structure (UI)

```
health-insurance-premium-prediction-ui/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── assets/
```

---

## 🚀 Deployment Summary

- Separate Azure Web Apps for:
  - UI
  - Model API
- Same Resource Group (cost-optimized)
- Linux-based App Service Plan
- GitHub Actions for automated build & deploy

---

## 📌 Use Case

This project demonstrates:
- End-to-end ML deployment
- Real-world API consumption
- Cloud-native ML application design
- Production-grade separation of concerns

Perfect for **portfolio**, **interviews**, and **real deployments**.

---

## 👤 Author

**Karan Tatyaso Kamble**  
Machine Learning Engineer | Cloud ML | Full-Stack ML Systems

---

⭐ If you like this project, give it a star and feel free to fork!
