import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.losses import MeanSquaredError
import joblib

# Load dataset
df = pd.read_csv("synthetic_hydroponics_data.csv")  

# Define features and target
X = df[['pH', 'EC', 'temperature', 'humidity', 'light', 'water_temperature']]
y = df['growth_rate']

# Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build Optimized Neural Network Model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    BatchNormalization(),

    Dense(32, activation='relu'),
    BatchNormalization(),

    Dense(1)  # Output layer for regression
])

# Compile model
model.compile(optimizer=Adam(learning_rate=0.001), loss=MeanSquaredError())

# Early Stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train model
history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test), callbacks=[early_stopping], verbose=1)

# Predictions
y_pred = model.predict(X_test)
joblib.dump(scaler, 'scaler.pkl')
model.save("trained_model.h5")  # still save model as keras h5
# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Optimized NN Mean Squared Error: {mse:.6f}")
print(f"Optimized NN R² Score: {r2:.6f}")

# Plot training loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Training Loss Over Epochs')
plt.show()
