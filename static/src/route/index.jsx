import { createBrowserRouter } from "react-router-dom";
import Home from "@/views/Home/index";
import Posts from "@/views/Home/posts/index";
import CreatePost from "@/views/Home/CreatPost/index";
import CreatCommunity from "@/views/Home/CreatCommunity/index";

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
      {
        path: "/home/createCommunity",
        element: <CreatCommunity />,
      },
    ],
  },
]);
