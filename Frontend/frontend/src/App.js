import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./components/login/Login";
import { getFromStore } from "./utils/util";
import { IS_ADMIN, USER_TOKEN } from "./constants/storage";
import UserInfo from "./components/dashboard/UserInfo";
import AddUser from "./components/dashboard/AddUser";
import DeleteUser from "./components/dashboard/DeleteUser";
import QueryLogs from "./components/dashboard/Queries";
import ViewAllUsers from "./components/dashboard/ViewAllUsers";
import Dashboard from "./components/dashboard/Dashboard";
import EntryLog from "./components/dashboard/adminDashboard/entryLog/EntryLog";
import User from "./components/dashboard/adminDashboard/user/User";

function PrivateRouter({ children, isAdminRequired }) {
  let isLoggedIn = false;
  if (getFromStore(USER_TOKEN)) {
    isLoggedIn = true;
  }
  const isAdmin = getFromStore(IS_ADMIN) === "true";
  if (isAdminRequired && isAdmin && isLoggedIn) {
    return children;
  } else if (isAdminRequired && !isAdmin) {
    window.location.href = "/";
  } else if (isLoggedIn) {
    return children;
  }
  window.location.href = "/";
}
console.log();
const router = createBrowserRouter([
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/dashboard",
    element: (
      <PrivateRouter>
        <Dashboard />
      </PrivateRouter>
    ),
    children: [
      {
        index: true,
        element: <EntryLog />,
      },
      {
        path: "userInfo",
        element: <User />,
      },
    ],
  },
  {
    path: "/queryLogs",
    element: (
      <PrivateRouter isAdminRequired={true}>
        <QueryLogs />
      </PrivateRouter>
    ),
  },
  {
    path: "*",
    element: <NotFoundPage />,
  },
]);

function NotFoundPage() {
  return <h1>404 - Page not found</h1>;
}

export default function App() {
  return <RouterProvider router={router} />;
}
