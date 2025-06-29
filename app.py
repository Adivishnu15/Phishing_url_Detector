import streamlit as st
import pickle
import pandas as pd
from features import extract_features

# Load model
with open("model/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature column names (must match training)
feature_names = [
    'IsDomainIP',
    'URLLength',
    'HasObfuscation',
    'IsHTTPS',
    'NoOfSubDomain',
    'HasSocialNet',
    'NoOfURLRedirect'
]

st.set_page_config(page_title="Phishing URL Detector")
st.title("🔍 Phishing URL Detector")
st.write("Paste a URL to detect whether it's **phishing** or **legitimate**.")

url = st.text_input("🔗 Enter a URL")

if st.button("🚨 Detect"):
    if not url:
        st.warning("Please enter a URL.")
    else:
        try:
            features = extract_features(url)

            # 🔧 Convert to DataFrame with feature names
            input_df = pd.DataFrame([features], columns=feature_names)

            result = model.predict(input_df)[0]
            if result == 1:
                st.success("✅ This URL is Legitimate")
            else:
                st.error("⚠️ Warning: This URL is Phishing")
        except Exception as e:
            st.error(f"Error: {e}")
