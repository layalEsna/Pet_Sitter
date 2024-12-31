
import './App.css';
import SignupForm from './SignupForm';
import PetSittersPage from './PetSittersPage';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
    <div>
      <h1>Signup Form</h1>
        <SignupForm />
         <Routes>
          <Route path="/petsitters" element={<PetSittersPage />} />
         </Routes>
    </div>
    </Router>
  );
}

export default App;
