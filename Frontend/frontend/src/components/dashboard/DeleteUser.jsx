import { useState } from "react";

export default function DeleteUser(){

    const [username, setUsername] = useState('');
    
    
    return(
        <div>
            <form>

            <label htmlFor="username">Username</label>
            <input value={username} onChange={e=>setUsername(e.target.value)} type="text" placeholder="Username" id="username" required/>
            
            
            
            <button>DELETE</button>
            </form>

        </div>
    );
}