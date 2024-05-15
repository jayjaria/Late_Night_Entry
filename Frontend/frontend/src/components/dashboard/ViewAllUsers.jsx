import { useEffect, useState } from "react";
import axiosInstance from "../../axios/interceptors";

export default function ViewAllUsers() {
  const [userLogs, setUserLogs] = useState([]);

  useEffect(() => {
    const fetchUserLogs = async () => {
      try {
        const response = await axiosInstance.get(
          "http://localhost:5000/users-info",
          {}
        );
        setUserLogs(response.data.user_log);
      } catch (error) {
        console.error("Error:", error);
      }
    };
    fetchUserLogs();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Username</th>
          <th>IsAdmin</th>
        </tr>
      </thead>
      <tbody>
        {userLogs.map((log, index) => (
          <tr key={index}>
            <td>{log.username}</td>
            <td>{log.role ? "Admin" : "User"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
