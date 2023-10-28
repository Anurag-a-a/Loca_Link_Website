import { createBrowserRouter } from "react-router-dom";
import Home from "@/views/Home/index";
import Posts from "@/views/Home/posts/index";
import CreatePost from "@/views/Home/CreatPost/index";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
    children: [
      {
        path: "/",
        element: <Posts />,
      },
      {
        path: "/home/createPost",
        element: <CreatePost />,
      },
    ],
  },
]);
