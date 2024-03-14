import React from 'react';
import './page3.css';
import seth from './images/seth.png';
import Ellipse from './images/Ellipse.png';
import machine from './images/machine.png';
import purple from './images/purple.png';
import lp from './images/lp.png';
import bc from './images/bc.png';
import heart from './images/heart.png';
import liver from './images/liver.png';
import kidney from './images/kidney.png';
import lungs from './images/lungs.png';
import malaria from './images/malaria.png';



 function DoctorConsultaion() {
  
  return (
   

    <div className="container">
      
      

      <div className='box'>
        <div>
        <img id='rec' src={purple} alt='pic'></img>
        </div>
        <div>
        <img id='pur' src={lp} alt='pic'></img>
        </div>
        
        <div id='RA'><text>Report Analyzer</text></div>
        
          <div >
            
            <button id= "but" >Diabetes</button>
            <button id= "but1">Breast Cancer </button>
            <button id= "but2">Heart</button>
            <button id= "but3">Kidney</button>
            <button id= "but4">Liver</button>
            <button id= "but5" >Malaria</button>
            <button id= "but6">Pneumonia</button>
          </div>
          <div >
            
            <img id='ell' src={Ellipse} alt='pic'></img>
            <img id='sth' src={seth}alt='pic' ></img>
            <img id='mach' src={machine}alt='pic' ></img>
            <img id='bcan' src={bc}alt='pic' ></img>
            <img id='heart' src={heart}alt='pic' ></img>
            <img id='liver' src={liver}alt='pic' ></img>
            <img id='lungs' src={lungs}alt='pic' ></img>
            <img id='malaria' src={malaria}alt='pic' ></img>
            <img id='kidney' src={kidney}alt='pic' ></img>
          </div>
          <div id='para1'>
            <h4 id='dia'>Diabetes</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para2'>
            <h4 id='bc'>Brest Cancer</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para3'>
            <h4 id='bc'>Heart</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para4'>
            <h4 id='bc'>Kidney</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para5'>
            <h4 id='bc'>Liver</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para6'>
            <h4 id='bc'>Malaria</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div id='para7'>
            <h4 id='bc'>Pneumonia</h4>
            <p >Lorem Ipsum is simply dummy text of the printing <br/>and typesetting industry. Lorem Ipsum has been<br /> the industry's standard dummy text ever since the 1500s, when <br/>an unknown printer took a galley of type and scrambled</p>
          </div>
          <div>
          </div>
      </div>
    </div>
    
    
  );
}

export default DoctorConsultaion;

