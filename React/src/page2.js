import './page2.css';
import React from 'react';

import SignUp from './signup';
import Feeling from './feeling';
import MoreInfo from './moreinfo';
import MoreInfo2 from './moreinfo2';
import MoreInfo3 from './moreinfo3';
import Welcome from './Welcome';
import Output from './output';
import { useState } from "react";

function Page2() {
  const [page, setPage] = useState(0);
  


  const componentList = [
    <Welcome page={page} setPage={setPage} />,
    <SignUp page={page} setPage={setPage} />,
    <Feeling page={page} setPage={setPage} />,
    <MoreInfo page={page} setPage={setPage} />,
    <MoreInfo2 page={page} setPage={setPage} />,
    <MoreInfo3 page={page} setPage={setPage} />,
    <Output page={page} setPage={setPage} />,
  ];
  
  return (
    <div className="Page2">
      
      
      <div>
        {componentList[page]}
      </div>
    </div>
  );
}

export default Page2;