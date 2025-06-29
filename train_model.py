# train_model.py
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

# Load dataset
data = fetch_ucirepo(id=967)
X_full = data.data.features
y = data.data.targets

# Select relevant columns that we can match in features.py
selected_features = [
    'IsDomainIP',             # Similar to having_IP_Address
    'URLLength',              # URL_Length
    'HasObfuscation',         # Used in phishing detection
    'IsHTTPS',                # Secure or not
    'NoOfSubDomain',          # Subdomain complexity
    'HasSocialNet',           # Social networks in URL
    'NoOfURLRedirect'         # Redirects
]

X = X_full[selected_features]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
os.makedirs("model", exist_ok=True)
with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model/phishing_model.pkl")
