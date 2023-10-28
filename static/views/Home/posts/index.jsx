/**
 *
 * @returns post list
 */
import "./index.scss";
import LeftTreeList from "@/views/Home/posts/components/TreeList/index";
import SelectionMain from "@/views/Home/posts/components/SelectionMain/index";

const Posts = () => {
  return (
    <div className="post-list">
      <LeftTreeList />
      <SelectionMain />
    </div>
  );
};

export default Posts;
