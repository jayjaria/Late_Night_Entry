import { useState, useEffect } from "react";
import axiosInstance from "../../../../axios/interceptors";
import {
  Modal,
  ModalBody,
  ModalTitle,
  ModalFooter,
  Button,
} from "react-bootstrap";

export default function User() {
  const [userLogs, setUserLogs] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [formState, setFormState] = useState({
    username: "",
    password: "",
    role: "User",
  });
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [deleteUser, setDeleteUser] = useState("");

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

  useEffect(() => {
    fetchUserLogs();
  }, []);

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    // const state = { ...formState, [name]: value };
    const state = Object.assign({}, formState);
    state[name] = value;
    setFormState(state);
  };

  const handleSubmit = async (e) => {
    if (!formState.username.trim() || !formState.password.trim()) {
      alert("Please provide all the required fields");
      return;
    }
    try {
      const response = await axiosInstance.post(
        "http://localhost:5000/add-user",
        {
          username: formState.username,
          password: formState.password,
          role: formState.role,
        }
      );
      await fetchUserLogs();
    } catch (error) {
      alert(error.response?.data?.message);
    } finally {
      setShowModal(false);
    }
  };

  const handleClose = () => {
    console.log("hanleClose");
    setShowModal(false);
    setFormState({
      username: "",
      password: "",
      role: "User",
    });
  };

  const handleDeleteModalClose = () => {
    setShowDeleteModal(false);
  };

  const handleDeleteModalSubmit = async () => {
    try {
      const response = await axiosInstance.delete(
        "http://localhost:5000/delete-user",
        {
          params: { username: deleteUser },
        }
      );
      await fetchUserLogs();
    } catch (error) {
      alert(error.response?.data?.message);
    } finally {
      setShowDeleteModal(false);
    }
  };

  function handleDelete(username) {
    setDeleteUser(username);
    setShowDeleteModal(true);
  }

  function renderModal() {
    return (
      <Modal show={showModal} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add User</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <form>
            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Username
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                name="username"
                value={formState.username}
                onChange={handleChange}
                required
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
                name="password"
                value={formState.password}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="role" className="form-label">
                Role
              </label>
              <select
                className="form-control"
                id="role"
                name="role"
                value={formState.role}
                onChange={handleChange}
                required
              >
                <option value="Admin">Admin</option>
                <option value="User">User</option>
              </select>
            </div>
          </form>
        </Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSubmit}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }

  function renderDeleteModal() {
    return (
      <Modal show={showDeleteModal} onHide={handleDeleteModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>Delete User</Modal.Title>
        </Modal.Header>
        <Modal.Body>Are you sure you want to delete {deleteUser}</Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={handleDeleteModalClose}>
            Close
          </Button>
          <Button variant="danger" onClick={handleDeleteModalSubmit}>
            Delete
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }

  return (
    <div className="container-fluid mt-5">
      <div className="d-flex justify-content-end">
        <button
          className="btn btn-outline-primary"
          onClick={() => {
            setShowModal(true);
          }}
        >
          Add User
        </button>
      </div>
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            <th>Username</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          {userLogs.map((log, index) => (
            <tr key={index}>
              <td>{log.username}</td>
              <td>{log.role ? "Admin" : "User"}</td>
              <td className="text-end">
                <Button
                  variant="danger"
                  onClick={() => {
                    handleDelete(log.username);
                  }}
                >
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {renderModal()}
      {renderDeleteModal()}
    </div>
  );
}
