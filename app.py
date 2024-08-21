from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)  # Apply CORS to the entire app

# Load the trained model
model = joblib.load('tip_prediction_model.pkl')

@app.route('/')
def index():
    return "Welcome to the Tip Prediction API"

# Endpoint for predicting tips
@app.route('/predict-tip', methods=['POST'])
def predict_tip():
    try:
        data = request.json
        print("Received data:", data)  # Log the received data for debugging

        # Ensure all required fields are present
        required_fields = ['totalBill', 'dayOfWeek', 'timeOfDay', 'numDiners', 'waiterExperience', 'customerSatisfaction']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Convert all inputs to numeric types and log the transformed values
        try:
            total_bill = float(data['totalBill'])
            day_of_week = int(data['dayOfWeek'])  # Temporarily assuming this is an integer
            time_of_day = int(data['timeOfDay'])  # Temporarily assuming this is an integer
            num_diners = int(data['numDiners'])
            waiter_experience = int(data['waiterExperience'])
            customer_satisfaction = int(data['customerSatisfaction'])
        except ValueError as ve:
            return jsonify({'error': f'Invalid input type: {ve}'}), 400
        
        features = np.array([
            total_bill,
            day_of_week,
            time_of_day,
            num_diners,
            waiter_experience,
            customer_satisfaction
        ]).reshape(1, -1)

        print("Features array:", features)  # Log the features array for debugging

        predicted_tip = model.predict(features)[0]
        return jsonify({'predictedTip': predicted_tip})

    except KeyError as e:
        return jsonify({'error': f'Missing key in JSON data: {str(e)}'}), 400

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
