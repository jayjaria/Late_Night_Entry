import React, { useState, useEffect } from "react";
import axiosInstance from "../../axios/interceptors";

const Querylogs = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [batchNo, setBatchNo] = useState("");
  const [entryLogs, setEntryLogs] = useState([]);

  useEffect(() => {
    const fetchEntryLogs = async () => {
      try {
        const response = await axiosInstance.get(
          "http://localhost:5000/entry-log",
          {
            params: { startDate, endDate, batchNo },
          }
        );
        // console.log(response)
        setEntryLogs(response?.data?.log);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchEntryLogs();
  }, [startDate, endDate, batchNo]);

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Start Date:
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>
        <label>
          End Date:
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
        <label>
          Batch Number:
          <input
            type="text"
            value={batchNo}
            onChange={(e) => setBatchNo(e.target.value)}
          />
        </label>
      </form>

      <table>
        <thead>
          <tr>
            <th style={{ paddingRight: "30px" }}>Roll No</th>
            <th style={{ paddingRight: "30px" }}>Student Name</th>
            <th style={{ paddingRight: "30px" }}>Created By</th>
            <th style={{ paddingRight: "30px" }}>Created At</th>
          </tr>
        </thead>
        <tbody>
          {entryLogs.map((log, index) => (
            <tr key={index}>
              <td>{log.rollNo}</td>
              <td>{log.studentName}</td>
              <td>{log.createdBy}</td>
              <td>{log.createdAt}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Querylogs;
