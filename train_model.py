import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load your dataset
data = pd.read_csv('historical_tips.csv')

# Debugging: Print the column names to ensure they are correct
print("Columns in the dataset:", data.columns)

# Assuming your dataset has the following columns
X = data[['total_bill', 'day_of_week', 'time_of_day', 'num_diners', 'waiter_experience', 'customer_satisfaction']]
y = data['tip_amount']

# Encode categorical features
day_of_week_encoder = LabelEncoder()
X.loc[:, 'day_of_week'] = day_of_week_encoder.fit_transform(X['day_of_week'])

time_of_day_encoder = LabelEncoder()
X.loc[:, 'time_of_day'] = time_of_day_encoder.fit_transform(X['time_of_day'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and encoders
joblib.dump(model, 'tip_prediction_model.pkl')
joblib.dump(day_of_week_encoder, 'day_of_week_encoder.pkl')
joblib.dump(time_of_day_encoder, 'time_of_day_encoder.pkl')
