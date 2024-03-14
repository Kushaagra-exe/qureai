import React from 'react'
import './moreinfo.css'
const MoreInfo = ({ page, setPage }) => {
  return (
    <div className="card">
      <div className="step-title"></div>
        <div id='mi'> Some More information</div>
        <div id='mi2'><span>Any medical history? (optional)</span></div>
      <div>
        <input id='sm'  type="text" />
      </div>
      <div>
      <button id='b1' onClick={() => setPage(page - 1)}>Previous</button>
      <button id='b2' onClick={() => setPage(page + 1)}>Next</button>
      <button id='b3' onClick={() => setPage(page + 1)}>Skip</button>
      </div>
    </div>
  );
};

export default MoreInfo;