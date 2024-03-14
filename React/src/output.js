import React from 'react'
import './output.css'
import group28 from './images/Group 28.png'
const Output = ({ page, setPage }) => {
  return (
    <div>
        <div>
          <img src={group28} alt='pic'></img>
        </div>
        <div>
          <button id='bu1' onClick={() => setPage(page + 1)}>Skip</button>
        </div>
        <div>
          <button id='bu2' onClick={() => setPage(page + 1)}>Next</button>
        </div>
      
    </div>
  );
};

export default Output;
