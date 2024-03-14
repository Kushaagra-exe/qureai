import React from 'react'
import './Welcome.css';
const Welcome = ({ page, setPage }) =>{
  return (
    <div>
      <div>
        <button className='but' onClick={() => setPage(page + 1)}>
          click me!
          
        </button>
      </div>
      
      <div className='tet'>
        <div><strong>Check Possible</strong></div>
        <div><strong> Disease!</strong></div>
      </div>
    </div>
  )
}

export default Welcome
