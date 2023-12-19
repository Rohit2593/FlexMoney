import React, { useState } from 'react';

const MyForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: '',
    batch: '',
    paymentDetails: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,  
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate form data
    for (const key in formData) {
      if (formData[key] === '') {
        alert(`Please fill in all fields.`);
        return;
      }
    }

    const formDataWithIntAge = {
      ...formData,
      age: parseInt(formData.age, 10),
      batch: parseInt(formData.batch, 10),
    };

    // Assuming you have a backend API endpoint for form submission
    try {
      const response = await fetch('http://localhost:8000/api/make-payment/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formDataWithIntAge),
      })

      const result = await response.json();
      alert(result.message)
      
      if(response.ok){
        if(result.message.includes("Payment successful")){
          setFormData({
            name: '',
            email: '',
            age: '',
            batch: '',
            paymentDetails: '',
          });
        }
      }
    } 
    catch (error) {
      console.error('Error:', error);
      alert('Error submitting form. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" name="name" value={formData.name} onChange={handleChange} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
      </label>
      <br />
      <label>
        Age:
        <input type="number" name="age" value={formData.age} onChange={handleChange} />
      </label>
      <br />
      <label>
        Batch:
        <select name="batch" value={formData.batch} onChange={handleChange}>
          <option value="">Select Batch</option>
          <option value="1">6-7 AM</option>
          <option value="2">7-8 AM</option>
          <option value="3">8-9 AM</option>
          <option value="4">5-6 PM</option>
        </select>
      </label>
      <br />
      <label>
        Payment Details (Rupees 500):
        <input
          type="text"
          name="paymentDetails"
          value={formData.paymentDetails}
          onChange={handleChange}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
};

export default MyForm;