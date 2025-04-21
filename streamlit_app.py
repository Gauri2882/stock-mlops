import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -------------------- Page Config & Styling --------------------
st.set_page_config(layout="wide", page_title="Stock Predictor")

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton > button {
        background-color: #0066cc;
        color: white;
        font-weight: bold;
    }
    .stDataFrame th, .stDataFrame td {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- Load Model & Scaler --------------------
model = joblib.load('models/model.pkl')
scaler = joblib.load('models/scaler.pkl')

# -------------------- UI Title --------------------
st.title('📈 Stock Predictor')

# -------------------- Input Section --------------------
feature_names = ['Open', 'High', 'Low', 'Adj Close', 'Volume']
features = [
    st.number_input(name, value=0.0, format="%.9f", key=name)
    for name in feature_names
]

# -------------------- Prediction & Validation --------------------
if st.button('🔍 Predict'):
    if any(val < 0 for val in features):
        st.warning("⚠️ Please enter only positive values.")
    else:
        input_array = np.array([features])
        scaled = scaler.transform(input_array)
        predicted_value = model.predict(scaled)[0]

        # Show results
        st.success(f"""
        🔬 **Predicted Price (Full Precision):** {predicted_value:.9f}  
        💰 **Rounded Price:** {predicted_value:.2f}
        """)

        # Save to history
        if 'history' not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            **{name: val for name, val in zip(feature_names, features)},
            'Predicted Price': predicted_value
        })

# -------------------- Prediction History --------------------
if 'history' in st.session_state and st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.subheader("📜 Prediction History")
    st.dataframe(history_df)

# -------------------- Batch Prediction --------------------
st.subheader("📂 Batch Prediction from CSV")
uploaded_file = st.file_uploader("Upload a CSV file with columns: Open, High, Low, Adj Close, Volume", type="csv")
if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        scaled_data = scaler.transform(data)
        predictions = model.predict(scaled_data)
        data['Predicted Price'] = predictions

        st.success("✅ Batch predictions completed!")
        st.dataframe(data)

        st.download_button(
            label="📥 Download Results as CSV",
            data=data.to_csv(index=False),
            file_name="batch_predictions.csv",
            mime='text/csv'
        )
    except Exception as e:
        st.error(f"❌ Error: {e}")
