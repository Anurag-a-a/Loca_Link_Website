/**
 *
 * @returns Home Page
 */
import "./index.scss";
import Navbar from "@/components/Navbar/index";
import { Outlet } from "react-router-dom";

const Home = () => {
  return (
    <div className="home">
      <Navbar />
      <div className="main-container">
        <Outlet />
      </div>
    </div>
  );
};

export default Home;
