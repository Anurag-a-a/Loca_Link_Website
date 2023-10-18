/**
 *
 * @returns create post
 */
import "./index.scss";
import {
  Paper,
  Box,
  AppBar,
  Toolbar,
  Typography,
  Tabs,
  Tab,
  TextField,
} from "@mui/material";
import {
  PostAdd as PostAddIcon,
  ImageOutlined as ImageOutlinedIcon,
  AddLinkOutlined as AddLinkOutlinedIcon,
} from "@mui/icons-material";
import { TextareaAutosize as BaseTextareaAutosize } from "@mui/base";
import FileUpload from "@/components/uploadFile/index";

import { styled } from "@mui/system";
import { useState } from "react";

const CreatPost = () => {
  const [tabVal, setTabVal] = useState(0);

  const handleChange = (e, newValue) => {
    setTabVal(newValue);
  };

  const blue = {
    100: "#DAECFF",
    200: "#b6daff",
    400: "#3399FF",
    500: "#007FFF",
    600: "#0072E5",
    900: "#003A75",
  };

  const grey = {
    50: "#f6f8fa",
    100: "#eaeef2",
    200: "#d0d7de",
    300: "#afb8c1",
    400: "#8c959f",
    500: "#6e7781",
    600: "#57606a",
    700: "#424a53",
    800: "#32383f",
    900: "#24292f",
  };

  const TextareaAutosize = styled(BaseTextareaAutosize)(
    ({ theme }) => `
  width: 320px;
  font-family: IBM Plex Sans, sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding: 12px;
  border-radius: 12px 12px 0 12px;
  color: ${theme.palette.mode === "dark" ? grey[300] : grey[900]};
  background: ${theme.palette.mode === "dark" ? grey[900] : "#fff"};
  border: 1px solid ${theme.palette.mode === "dark" ? grey[700] : grey[200]};
  box-shadow: 0px 2px 24px ${
    theme.palette.mode === "dark" ? blue[900] : blue[100]
  };

  &:hover {
    border-color: ${blue[400]};
  }

  &:focus {
    border-color: ${blue[400]};
    box-shadow: 0 0 0 3px ${
      theme.palette.mode === "dark" ? blue[600] : blue[200]
    };
  }

  // firefox
  &:focus-visible {
    outline: 0;
  }
`
  );

  return (
    <div className="create-post">
      <AppBar position="static" sx={{ width: 800, margin: "20px auto" }}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Create Post
          </Typography>
        </Toolbar>
      </AppBar>
      <Box
        sx={{
          width: 800,
          height: "calc(100% - 74px)",
          margin: "10px auto",
          "& > :not(style)": {
            width: "100%",
          },
        }}
      >
        <Paper elevation={3}>
          <Tabs value={tabVal} onChange={handleChange} centered>
            <Tab icon={<PostAddIcon />} iconPosition="start" label="Post" />
            <Tab
              icon={<ImageOutlinedIcon />}
              iconPosition="start"
              label="Image & Video"
            />
            <Tab
              icon={<AddLinkOutlinedIcon />}
              iconPosition="start"
              label="Link"
            />
          </Tabs>
          <div
            className="tab-content-wrap"
            style={{
              // marginTop: "20px",
              padding: "20px",
            }}
          >
            <div>
              <TextField fullWidth label="title" variant="filled" />
            </div>
            &nbsp;
            <div>
              {tabVal === 0 && (
                <TextareaAutosize
                  fullWidth
                  aria-label="empty textarea"
                  minRows={3}
                  placeholder="Text Content"
                  sx={{
                    width: "calc(100% - 20px)",
                  }}
                />
              )}
              {tabVal === 1 && <FileUpload />}
              {tabVal === 2 && <TextField fullWidth label="Url" />}
            </div>
          </div>
        </Paper>
      </Box>
    </div>
  );
};

export default CreatPost;
