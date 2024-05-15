import { NavLink } from "react-router-dom";
import { clearStorage } from "../../../utils/util";
import "./Navbar.css";

export default function Navbar(props) {
  const handleLogout = () => {
    clearStorage();
    window.location.href = "/";
  };
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          <img src={process.env.PUBLIC_URL + "/iiitg_complete_logo.png"} />
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          {props.isAdmin && (
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  end
                  to="/dashboard"
                  activeClassName="active"
                >
                  Late Night Entries
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  exact
                  to="/dashboard/userInfo"
                  activeClassName="active"
                >
                  Users
                </NavLink>
              </li>
            </ul>
          )}
        </div>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <button
            className="btn btn-outline-primary mr-2 d-lg-none mt-3"
            onClick={handleLogout}
          >
            Logout
          </button>
        </div>

        <button
          className="btn btn-outline-primary ml-auto d-none d-lg-block"
          onClick={handleLogout}
        >
          Logout
        </button>
      </div>
    </nav>
  );
}
