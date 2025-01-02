
import './App.css';
import SignupForm from './SignupForm';
import PetSittersPage from './PetSittersPage';
import Appointment from './Appointment';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <h1>Signup Form</h1>

        {/* <SignupForm />
        <PetSittersPage />
        <Appointment/> */}

        <Routes>
          <Route path="/signup" element={<SignupForm />} />
          <Route path="/pet_sitters" element={<PetSittersPage />} />
          <Route path="/appointment" element={<Appointment />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
