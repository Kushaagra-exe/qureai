import React from 'react'
import './moreinfo3.css'
const MoreInfo = ({ page, setPage }) => {
  return (
    <div className="card">
      <div className="step-title"></div>
        <div id='si'> Some More information</div>
        <div id='si2'><span>Potential exposure? (optional)</span></div>
      <div>
        <input id='sm'  type="text" />
      </div>
      <div>
      <button id='b1' onClick={() => setPage(page - 1)}>Previous</button>
      <button id='b2' onClick={() => setPage(page + 1)}>Submit</button>
      </div>
    </div>
  );
};

export default MoreInfo;