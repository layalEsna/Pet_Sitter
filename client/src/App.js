

import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignupForm from "./SignupForm";


function App() {
  return (
  <Router>
    <Routes>
      <Route path='/signup' Component={SignupForm}/>
    </Routes>
  </Router>
  );
}

export default App;
