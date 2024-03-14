import React from 'react'
import './moreinfo2.css'
const MoreInfo = ({ page, setPage }) => {
  return (
    <div className="card">
      <div className="step-title"></div>
        <div id='smi'> Some More information</div>
        <div id='smi2'><span>where have you been, recently? (optional)</span></div>
      <div>
        <input id='sm'  type="text" />
      </div>
      <div>
      <button id='b1' onClick={() => setPage(page - 1)}>Previous</button>
      <button id='b2' onClick={() => setPage(page + 1)}>Next</button>

      </div>
    </div>
  );
};

export default MoreInfo;