import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Page1 from "./page1";
import Page2 from "./page2";
import Page3 from "./page3";

import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <div className='min-h-[88vh]'>
          <Routes>
            <Route path="/page1" element={<Page1 />} />
            <Route path="/page2" element={<Page2 />} />
            <Route path="/page3" element={<Page3 />} />
            {/* Default Route */}
            <Route path="/" element={<Page1 />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
