import { useState } from "react";

export default function AddUser() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  return (
    <div>
      <form>
        <label htmlFor="username">Username</label>
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          type="text"
          placeholder="Username"
          id="username"
          required
        />

        <label htmlFor="password">Password</label>
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="text"
          placeholder="Password"
          id="password"
          required
        />

        <label htmlFor="role">Role</label>
        <input
          value={role}
          onChange={(e) => setRole(e.target.value)}
          type="text"
          placeholder="Role"
          id="role"
          required
        />

        <button>ADD</button>
      </form>
    </div>
  );
}
