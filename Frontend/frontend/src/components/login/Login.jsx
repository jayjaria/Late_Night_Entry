import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { jwtDecode } from "jwt-decode";
import { getFromStore, saveToStore } from "../../utils/util";
import { IS_ADMIN, USER_TOKEN } from "../../constants/storage";
import "./Login.css";
import Card from "../dashboard/card/Card";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  useEffect(() => {
    if (getFromStore(USER_TOKEN)) {
      navigate("/dashboard");
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/login", {
        username,
        password,
      });
      saveToStore(USER_TOKEN, response?.data?.token);
      const token = jwtDecode(response.data.token);
      saveToStore(IS_ADMIN, token.is_admin);
      console.log(token);

      navigate("/dashboard");
    } catch (error) {
      if (error.response.status === 404) {
        alert(error.response.data.message);
      } else if (error.response.status === 400) {
        alert(error.response.data.message);
      }
      setPassword("");
      setUsername("");
    }
  };

  return (
    <div className="card-container container-fluid ">
      <Card>
        <form>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              Username
            </label>
            <input
              type="text"
              className="form-control"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div className="d-flex justify-content-center">
            <button
              type="submit"
              className="btn btn-primary"
              onClick={handleSubmit}
            >
              Submit
            </button>
          </div>
        </form>
      </Card>
    </div>
  );
}

export default Login;
