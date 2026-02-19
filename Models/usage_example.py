import joblib
import numpy as np

# Load model and preprocessors
model = joblib.load('models/trained_model.pkl')
scaler = joblib.load('models/scaler.pkl')
topo_extractor = joblib.load('models/topological_extractors.pkl')

# Prepare patient data
patient_features = np.array([[...]])  # Your 76 features
patient_features_scaled = scaler.transform(patient_features)

# Get prediction
risk_probability = model.predict_proba(patient_features_scaled)[0, 1]
print(f"1-year mortality risk: {risk_probability:.2f}")