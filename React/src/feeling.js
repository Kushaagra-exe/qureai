import React from 'react'
import './feeling.css';
const Feeling = ({ page, setPage }) => {
  return (
    <div className="card">
      <div className="step-title"></div>
        <div id='tt1'><span>Tell us how are you feeling?</span></div>
        <div id='tt2'><span>Symtoms</span></div>
      <div>
      <input  id='inn' type="text" />
      </div>
      <div className='bs'>
      <button id= 'butt'onClick={() => setPage(page - 1)}>Previous</button>
      <button id= 'butt1' onClick={() => setPage(page + 1)}>Next</button>
      </div>
    </div>
  );
};

export default Feeling;