import { useState, useEffect } from "react"

function PetSittersPage() {

    const [petSitters, setPetSitters] = useState([])

    useEffect(() => {
        fetch('http://localhost:5002/pet_sitters')
            .then(res => res.json())
            .then(data => setPetSitters(data))
        .catch(e => console.error(e))
    }, [])

    return (
        <div>
            <ul>
            {petSitters.map(sitter => (
                <li key={sitter.id}>
                    <h3>{sitter.sitter_name}</h3>
                    <p>Location: {sitter.location}</p>
                    <p>Price: ${sitter.price} per day</p>
                    <button>Book Appointment</button>
                </li>
            ))}
            </ul>
            
        </div>
    )
    
}

export default PetSittersPage