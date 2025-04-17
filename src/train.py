# src/train.py
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/clean_data_one.csv")  # Move your CSV to the `data/` folder

# Preprocess
X = df.drop('Close', axis=1)
y = df['Close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale and train
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save artifacts
joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
print("Model and scaler saved!")