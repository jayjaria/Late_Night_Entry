import React, { useState } from "react";
import axiosInstance from "../../../axios/interceptors";
import Card from "../card/Card";
import "./UserDashboard.css";
export default function UserDashboard() {
  const [rollNumber, setRollNumber] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post(
        "http://localhost:5000/entry-log",
        { rollNo: rollNumber }
      );
      console.log(response);
      alert("THANK YOU!! Your Late Night Entry is recorded.");
    } catch (error) {
      if (error.response.status === 404) {
        alert(error.response.data.message);
      } else if (error.response.status === 400) {
        alert(error.response.data.message);
      }
    }
    setRollNumber("");
  };
  return (
    <div className="card-container-user-dashboard container-fluid d-flex justify-content-center align-items-center">
      <Card headerNotRequired={true}>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="mb-3">
            <label htmlFor="rollNo" className="form-label">
              Roll no
            </label>
            <input
              type="text"
              className="form-control"
              id="rollNo"
              value={rollNumber}
              onChange={(e) => setRollNumber(e.target.value)}
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
