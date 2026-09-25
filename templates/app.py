import random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
CORS(app)

# Load Datasets
symptoms_data = pd.DataFrame({
    'description': ['head pain fever', 'stomach pain indigestion', 'cough cold fever', 'dry skin joint pain'],
    'symptom': ['Shiroroga', 'Ajeerna', 'Kasa/Jwara', 'Vata Vyadhi']
})

indications_data = pd.DataFrame({
    'formulation': ['Pathyadi Kvatha', 'Shadanga Churna', 'Pippali Mula Churna', 'Bhringaraja Taila', 'Shadbindu Taila', 'Akika Pishti'],
    'main_indications': ['shiroroga', 'shiroroga', 'shiroroga', 'shiroroga', 'shiroroga', 'shiroroga']
})

# Preprocess and Train Model
X = symptoms_data['description'].str.lower()
y = symptoms_data['symptom']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

# Sample Doctor List
sample_doctors = [
    {"name": "Dr. Nitin Deshmukh", "phone": "7000000006"},
    {"name": "Dr. Priya Kaur", "phone": "7000000007"},
    {"name": "Dr. Manish Verma", "phone": "7000000010"},
    {"name": "Dr. Anita Joshi", "phone": "7000000001"},
    {"name": "Dr. Ravi Patel", "phone": "9123456780"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_desc = data.get('description', '').lower()

    if not user_desc:
        return jsonify({'error': 'No description provided'}), 400

    # Vectorize and Predict
    user_vec = vectorizer.transform([user_desc])
    predicted_symptom = model.predict(user_vec)[0]

    # Filter Medicines
    matched_meds = indications_data[indications_data['main_indications'].str.contains(predicted_symptom.lower(), na=False)]['formulation'].tolist()
    if not matched_meds:
        matched_meds = ["Pathyadi Kvatha", "Shadanga Churna", "Pippali Mula Churna", "Bhringaraja Taila", "Shadbindu Taila"]

    # Select Random Doctors
    selected_doctors = random.sample(sample_doctors, min(len(sample_doctors), 5))

    return jsonify({
        'predicted_symptom': predicted_symptom,
        'recommended_medicines': matched_meds[:5],
        'recommended_doctors': selected_doctors
    })

if __name__ == '__main__':
    app.run(debug=True)

