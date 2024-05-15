import { useEffect, useState } from "react";
import axiosInstance from "../../../../axios/interceptors";
import { MAX_YEAR } from "../../../../constants/dashboard";
import Table from "../../table/Table";

export default function EntryLog() {
  let today = new Date();
  const [formState, setFormState] = useState({
    startDate: "",
    endDate: "",
    batchNo: "",
  });
  const [entryLogs, setEntryLogs] = useState([]);

  const getParams = (paramObj) => {
    const params = {};
    Object.keys(paramObj).forEach((key) => {
      if (paramObj[key]) {
        params[key] = paramObj[key];
      }
    });
    return params;
  };
  useEffect(() => {
    const fetchLastNightEntries = async () => {
      try {
        const response = await axiosInstance.get(
          "http://localhost:5000/entry-log",
          {
            params: getParams(formState),
          }
        );
        // console.log("here");
        // console.log(response);
        setEntryLogs(response.data.log);
      } catch (error) {
        console.error("Error:", error);
      }
    };
    fetchLastNightEntries();
  }, [formState.startDate, formState.endDate, formState.batchNo]);

  // useEffect(() => {
  //   const fetchEntryLogs = async () => {
  //     try {
  //       const response = await axiosInstance.get(
  //         "http://localhost:5000/entry-log",
  //         {
  //           params: { startDate, endDate, batchNo },
  //         }
  //       );
  //       // console.log(response)
  //       setEntryLogs(response?.data?.log);
  //     } catch (error) {
  //       console.error("Error:", error);
  //     }
  //   };

  //   fetchEntryLogs();
  // }, [startDate, endDate, batchNo]);

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  const handleChange = (event) => {
    console.log("event", event);
    const name = event.target.name;
    let value = event.target.value;

    if (name == "batchNo") {
      value = value.slice(-2);
    }

    const state = { ...formState, [name]: value };
    setFormState(state);
  };

  const options = [];
  const year = today.getFullYear();
  for (let i = 0; i < MAX_YEAR; i++) {
    options.push(year - i);
  }
  console.log("options", options);

  return (
    <div className="container-fluid mt-5">
      {/* <form onSubmit={handleSubmit}>
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
      </form> */}
      <div className="d-flex justify-content-between">
        <div className="input-group mb-3 me-4">
          <span className="input-group-text" id="basic-addon1">
            Batch Number
          </span>
          <select
            name="batchNo"
            className="form-select"
            aria-label="Default select example"
            onChange={handleChange}
          >
            {options.map((option) => (
              <option value={option} key={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="input-group mb-3 me-4">
          <span className="input-group-text" id="basic-addon1">
            Start Date
          </span>
          <input
            name="startDate"
            type="date"
            className="form-control"
            placeholder="Username"
            aria-label="Username"
            aria-describedby="basic-addon1"
            onChange={handleChange}
          />
        </div>

        <div className="input-group mb-3">
          <span className="input-group-text" id="basic-addon1">
            End Date
          </span>
          <input
            name="endDate"
            type="date"
            className="form-control"
            placeholder="Username"
            aria-label="Username"
            aria-describedby="basic-addon1"
            onChange={handleChange}
          />
        </div>
      </div>

      <Table
        data={entryLogs}
        columns={["Roll No", "Student Name", "Created By", "Created At"]}
      />
      {/* <table>
        <thead>
          <tr>
            <th style={{ paddingRight: "30px" }}>Roll No</th>
            <th style={{ paddingRight: "30px" }}>Student Name</th>
            <th style={{ paddingRight: "30px" }}>Created By</th>
            <th style={{ paddingRight: "30px" }}>Created At</th>
          </tr>
        </thead>
        <tbody>
          {lastNightEntries.map((log, index) => (
            <tr key={index}>
              <td>{log.rollNo}</td>
              <td>{log.studentName}</td>
              <td>{log.createdBy}</td>
              <td>{log.createdAt}</td>
            </tr>
          ))}
        </tbody>
      </table> */}
    </div>
  );
}
