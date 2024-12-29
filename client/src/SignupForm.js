import { useState } from "react";
import "./index.css";


function SignupForm() {
    
    const [formData, setFormData] = useState({
        user_name: '',
        password: '',
        confirm_password: '',
        pet_name: '',
        pet_type: '',
        zip_code: ''

    })

    function handleFormData(e) {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    return (
        <form>
            <div>
                <label>Create username</label>
                <input
                    name="user_name"
                    value={formData.user_name}
                    type="text"
                    onChange={handleFormData}
                />
            </div>
            <br/>
            <div>
                <label>Create password</label>
                <input
                    name="password"
                    value={formData.password}
                    type="password"
                    onChange={handleFormData}
                />
            </div>
            <br/>
            <div>
                <label>Confirm password</label>
                <input
                    name="confirm_password"
                    value={formData.confirm_password}
                    type="password"
                    onChange={handleFormData}
                />
            </div>
            <br/>
            <div>
                <label>Pet name</label>
                <input
                    name="pet_name"
                    value={formData.pet_name}
                    type="text"
                    onChange={handleFormData}
                />
            </div>
            <br/>
            <div>
                <label>Create username</label>
                <select
                    name="pet_type"
                    value={formData.pet_type}
                    onChange={handleFormData}
                >
                    <option value="">Select one</option>
                    <option value="cat">cat</option>
                    <option value="dog">dog</option>
                    <option value="bird">bird</option>
                </select>
            </div>
            <br/>
            <div>
                <label>Zip code</label>
                <input
                    name="zip_code"
                    value={formData.zip_code}
                    type="text"
                    onChange={handleFormData}
                />
            </div>
            <br/>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
    )



}
export default SignupForm