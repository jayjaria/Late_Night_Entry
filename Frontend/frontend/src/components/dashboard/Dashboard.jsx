import { IS_ADMIN, USER_TOKEN } from "../../constants/storage";
import { getFromStore } from "../../utils/util";
import AdminDashboard from "./adminDashboard/AdminDashboard";
import UserDashboard from "./userDashboard/UserDashboard";
import Navbar from "./navbar/Navbar";

export default function Dashboard() {
  const isAdmin = getFromStore(IS_ADMIN) === "true";
  return (
    <div className="d-flex flex-column h-100">
      <Navbar isAdmin={isAdmin} />
      {isAdmin ? <AdminDashboard /> : <UserDashboard />}
    </div>
  );
}
