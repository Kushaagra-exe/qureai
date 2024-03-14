import React from 'react';
import { useNavigate } from 'react-router-dom';

function Page1() {
  const navigate = useNavigate();

  const goToPage2 = () => {
    navigate('/page2'); 
  }
  const goToPage3 = () => {
    navigate('/page3'); 
  };

  return (
    <div>
      <h1>This is Page 1</h1>
      <p>This is the content of Page 1.</p>
      <button onClick={goToPage2}>Go to Page 2</button>
      <button onClick={goToPage3}>Go to Page 3</button>
    </div>
  );
}

export default Page1;
