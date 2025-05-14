# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError

# Load trained model
model = load_model("trained_model.h5")

st.set_page_config(page_title="Hydroponic AI Dashboard", layout="wide")
st.title("Simulated Dashboard")

# Sidebar for simulated sensor input
st.sidebar.header("Simulated Sensor Inputs")
temperature = st.sidebar.slider("Temperature (°C)", 10, 40, 25)
water_temperature = st.sidebar.slider("Water temperature (°C)", 10, 40, 20)
humidity = st.sidebar.slider("Humidity (%)", 20, 100, 60)
light_intensity = st.sidebar.slider("Light Intensity (lux)", 100, 10000, 2000)
pH = st.sidebar.slider("pH Level", 4.0, 9.0, 6.5)
EC = st.sidebar.slider("Electrical Conductivity (mS/cm)", 0.1, 3.0, 1.5)

# Feature input for model
input_features = pd.DataFrame({
    'temperature': [temperature],
    'humidity': [humidity],
    'light_intensity': [light_intensity],
    'pH': [pH],
    'EC': [EC],
    'water_temperature' : [water_temperature],
})

# Predict nutrient requirement
predicted_nutrient = model.predict(input_features)[0][0]

st.metric("Predicted Nutrient Requirement (ml)", f"{predicted_nutrient:.2f}")

st.metric("Predicted Nutrient Requirement (ml)", f"{predicted_nutrient:.2f}")


# Show input values
st.subheader("Sensor Input Summary")
st.dataframe(input_features)

# Plotting dynamic chart
st.subheader("📊 Simulated Sensor Variation")
chart_data = pd.DataFrame(
    np.random.randn(20, 6)*0.5 + [temperature, water_temperature, humidity, light_intensity, pH, EC],
    columns=['Temperature', 'Water Temperature', 'Humidity', 'Light Intensity', 'pH', 'EC']
)
st.line_chart(chart_data)

# Add saved graphs
st.subheader("📉 Model Performance")
st.image("val_loss_curve.png", caption="Validation Loss Curve", use_container_width=True)
st.image("corelation.png", caption="Correlation Heatmap", use_container_width=True)


# System Logs (simulated)
st.subheader("📜 System Logs")
st.code(f"Actuator Triggered: Added {predicted_nutrient:.2f} ml nutrients at pH {pH}, EC {EC}")

st.success("Dashboard Ready - Demo Without Hardware ✨")
