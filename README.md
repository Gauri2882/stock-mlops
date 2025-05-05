# 📈 Stock Price Prediction MLOps Pipeline

An end-to-end machine learning project that predicts stock prices using Python, FastAPI, Docker, Kubernetes, and Streamlit.

---
## 🎯 SDG Alignment: Decent Work and Economic Growth (SDG 8)

[![SDG 8](https://img.shields.io/badge/SDG%208-Decent%20Work%20and%20Economic%20Growth-E5243B?style=for-the-badge&logo=unitednations)](https://sdgs.un.org/goals/goal8)

This project contributes to **United Nations Sustainable Development Goal 8** by:

- 📊 Helping individuals and businesses make **data-driven stock market decisions**
- 💸 Enabling better **financial planning and forecasting** through predictive analytics
- 🔍 Reducing unnecessary expenses by minimizing poor investment choices
- 📈 Promoting **economic productivity** and informed participation in financial markets

> By empowering users with accessible, AI-powered tools, this project supports inclusive and sustainable economic growth.
---
## 🚀 Features

- **Machine Learning**: Linear Regression model trained on historical stock data
- **Web API**: FastAPI endpoint for predictions
- **Containerized**: Docker packaging for consistent deployments
- **Scalable**: Kubernetes-ready deployment
- **Web Interface**: Streamlit dashboard for easy interaction


---

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes (Minikube for local testing)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/stock-mlops.git
cd stock-mlops
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Train the model

```bash
python src/train.py
```

---

## 🏃 Running the Project

### ✅ Option 1: Streamlit Interface (Recommended for demo)

```bash
streamlit run src/streamlit_app.py
```

### ✅ Option 2: Docker Container

```bash
docker build -t stock-model .
docker run -p 8000:8000 stock-model
```

### ✅ Option 3: Kubernetes Deployment (using Minikube)

```bash
minikube start
kubectl apply -f kubernetes/
minikube service stock-service –url
```

---

## 🌐 API Usage

**POST /predict**

```bash
curl -X POST "http://127.0.0.1:51864/predict"
-H "Content-Type: application/json"
-d "{\"features\": [0.047326903, 0.046355169, 0.046455092, 0.022161945, 0.015932633]}" 
```

**Response:**

```json
{
  "prediction": 0.04629013513070648
}
```

---

## 🖥️ Streamlit Interface Preview

![image](https://github.com/user-attachments/assets/652ce245-7f05-49ab-9c20-3dbc6d38c721)


- Input fields with high precision (9 decimal places)
- Real-time predictions
- Historical performance visualization

---

## 🤖 Technologies Used

| Technology    | Purpose                        |
|---------------|--------------------------------|
| Python        | Core programming language      |
| Scikit-learn  | Machine learning model         |
| FastAPI       | REST API endpoint              |
| Docker        | Containerization               |
| Kubernetes    | Orchestration                  |
| Streamlit     | Web interface                  |
| Minikube      | Local Kubernetes cluster       |

