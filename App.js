import React, { useState } from 'react';
import axios from 'axios';
import './style.css';

function App() {
  const [formData, setFormData] = useState({
    totalBill: '',
    dayOfWeek: '',
    timeOfDay: '',
    numDiners: '',
    waiterExperience: '',
    customerSatisfaction: ''
  });

  const [predictedTip, setPredictedTip] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log("Sending data:", formData);  // Log the data being sent for debugging

      const response = await axios.post('http://localhost:5000/predict-tip', formData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log("Response:", response.data);  // Log the response data for debugging
      setPredictedTip(response.data.predictedTip);
    } catch (error) {
      if (error.response) {
        console.error('Error response:', error.response.data);  // Error response from the server
      } else if (error.request) {
        console.error('Error request:', error.request);  // No response from the server
      } else {
        console.error('Error message:', error.message);  // Other errors
      }
    }
  };

  return (
    <div className='boxe'>
      <h1>Tip Prediction</h1>
      <form onSubmit={handleSubmit}>
      <label htmlFor="">Total Amount of bill(in $)</label>
        <input name="totalBill" value={formData.totalBill} onChange={handleChange} placeholder="Total Bill"  required/>
        <label htmlFor="">Day Of Week (1 to 7)</label>
        <input name="dayOfWeek" value={formData.dayOfWeek} onChange={handleChange} placeholder="Day of Week" required />
        <label htmlFor="">Time Of Day (In 24 hours )</label>
        <input name="timeOfDay" value={formData.timeOfDay} onChange={handleChange} placeholder="Time of Day" required/>
        <label htmlFor="">Num Diners (No. of people on table)</label>
        <input name="numDiners" value={formData.numDiners} onChange={handleChange} placeholder="Number of Diners"  required/>
        <label htmlFor="">Waiter Experience (Experience in years)</label>
        <input name="waiterExperience" value={formData.waiterExperience} onChange={handleChange} placeholder="Waiter Experience" required />
        <label htmlFor="">Customer Satisfaction (customer rating from 1 to 10)</label>
        <input name="customerSatisfaction" value={formData.customerSatisfaction} onChange={handleChange} placeholder="Customer Satisfaction"  required/>
        <button type="submit">Predict Tip</button>
      </form>
      {predictedTip !== null && <h2>Predicted Tip: ${Math.round(predictedTip * 100) / 100 }</h2>}
    </div>
  );

  
}

export default App;
