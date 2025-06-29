---
## Setup Locally
in terminal/command prompt

git clone https://github.com/Adivishnu15/phishing-url-detector.git
cd phishing-url-detector
pip install -r requirements.txt
streamlit run app.py

# Phishing URL Detector

This is a web-based application that detects whether a given URL is **phishing** or **legitimate** using a machine learning model. The project combines **URL feature extraction**, **machine learning**, and an interactive **Streamlit** web interface.

 **Live Demo**: [https://phishing-url-detector-szsm.onrender.com](https://phishing-url-detector-szsm.onrender.com)

---

## What We Built

We built an end-to-end phishing detection tool that:
- Takes user input (a URL)
- Extracts meaningful features from that URL
- Uses a machine learning model to predict if it’s a phishing link
- Displays the result instantly in a user-friendly web interface

This project is ideal for learning how ML models integrate into real-time web apps.

---

##  Tools & Technologies Used

-  **Machine Learning**: `scikit-learn`, `joblib`
-  **Web Interface**: `Streamlit`
-  **Dependency Management**: `requirements.txt`
-  **Deployment**: `Render.com`
-  **Version Control**: `Git + GitHub`

---

##  How It Works (Behind the Scenes)

1. **Feature Extraction from URL**  
   The app extracts features like:
   - Length of the URL
   - Presence of `@` symbol
   - Use of HTTPS or not
   - Number of subdomains
   - Suspicious characters or patterns

2. **Machine Learning Model**  
   A **Logistic Regression** (or any other classifier you trained) model was trained using labeled datasets of phishing and legitimate URLs. It’s serialized using `joblib` into `phishing_model.pkl`.

3. **Prediction Process**
   - The URL is converted into a vector using the same preprocessing (`vectorizer.pkl`) used during training.
   - The ML model predicts whether the URL is phishing or safe.

4. **User Interface**
   - A simple and fast UI built with **Streamlit**
   - Takes URL input and shows results in real time

---


