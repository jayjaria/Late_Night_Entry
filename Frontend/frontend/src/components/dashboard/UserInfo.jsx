import { useNavigate } from "react-router-dom";


export default function UserInfo(){

    const navigate = useNavigate();
    
    const handleAddUser = async (e) =>{
        e.preventDefault();
        navigate("/addUser")
    }

    const handleDeleteUser = async (e) => {
        e.preventDefault();
        navigate("/deleteUser");
    }

    const handleViewAllUsers = async(e) => {
        e.preventDefault();
        navigate("/viewAllUsers");
    }

    return(
        <div>
            <form>
                <h1>This is UserInfo.</h1>
                <button onClick={handleAddUser}>Add User</button>
                <button onClick={handleDeleteUser}>Delete User</button>
                <button onClick={handleViewAllUsers}>View All Users</button>
            </form>
        </div>
        
    );
}