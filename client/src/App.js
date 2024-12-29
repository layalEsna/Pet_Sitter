
import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SignupForm from "./SignupForm";


function App() {
  return (
  <Router>
    <Switch>
      <Route path='/signup' Component={SignupForm}/>
    </Switch>
  </Router>
  );
}

export default App;
