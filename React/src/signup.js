import React from 'react';
import './signup.css';

const SignUp = ({ page, setPage }) => {
  const handleNext = () => {
    console.log('hebfheb');
    setPage(page + 1);
  };

  return (
    <div className="card">
      <div className="step-title"></div>

      <input type="text" id='in1'/>

      <div id='t1'><strong>Name:</strong></div>

      <input type="text" id='in2' />

      <div id='t2'><strong>Age:</strong></div>

      <div className='rad'>
      <input type="radio" name="fruit" value="apple" />M
      <input type="radio" name="fruit" value="orange" />F
      </div>

      <div id='t3'><strong>Sex:</strong></div>
      
      <button id='but' onClick={handleNext}>Next</button>
    </div>
  );
};

export default SignUp;