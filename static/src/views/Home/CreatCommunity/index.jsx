/**
 *
 * @returns Creat Community
 */
import "./index.scss";
import {
  Paper,
  Box,
  AppBar,
  Toolbar,
  Typography,
  TextField,
  RadioGroup,
  Radio,
  FormLabel,
  FormControl,
  FormControlLabel,
  IconButton,
} from "@mui/material";
import {
  PostAdd as PostAddIcon,
  ImageOutlined as ImageOutlinedIcon,
  AddLinkOutlined as AddLinkOutlinedIcon,
  CheckCircleRounded as CheckCircleRoundedIcon,
  Cancel as CancelIcon,
} from "@mui/icons-material";
import BaseEditor from "@/components/Editor/index";

import { useState, useRef } from "react";

const CreatPost = () => {
  const editorRef = useRef(null);

  const log = () => {
    if (editorRef.current) {
      console.log(editorRef.current.getContent());
    }
  };

  return (
    <div className="create-post">
      &emsp;
      <AppBar position="static" sx={{ width: 800, margin: "0 auto" }}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Create Community
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
          <div
            className="tab-content-wrap"
            style={{
              // marginTop: "20px",
              padding: "20px",
            }}
          >
            <div>
              <TextField fullWidth label="Theme" variant="filled" />
              &nbsp;
              <TextField fullWidth label="notes" />
              &nbsp;
              <TextField fullWidth label="date" />
              &nbsp;
              <TextField fullWidth label="members" />
              &nbsp;
              <TextField fullWidth label="ads" />
              &nbsp;
              <FormControl>
                <FormLabel id="demo-row-radio-buttons-group-label">
                  set security
                </FormLabel>
                <RadioGroup
                  row
                  aria-labelledby="demo-row-radio-buttons-group-label"
                  name="row-radio-buttons-group"
                >
                  <FormControlLabel
                    value="public"
                    control={<Radio />}
                    label="public"
                  />
                  <FormControlLabel
                    value="private"
                    control={<Radio />}
                    label="private"
                  />
                </RadioGroup>
              </FormControl>
              &nbsp;
              <BaseEditor
                onInit={(evt, editor) => (editorRef.current = editor)}
                initialValue=""
                init={{
                  height: 500,
                  menubar: false,
                  branding: false,
                  a11y_advanced_options: true,
                  file_picker_types: "image",
                  plugins: [
                    "advlist",
                    "anchor",
                    "autolink",
                    "help",
                    "image",
                    "link",
                    "lists",
                    "searchreplace",
                    "table",
                    "wordcount",
                  ],
                  toolbar:
                    "undo redo | blocks | " +
                    "bold italic forecolor image | alignleft aligncenter " +
                    "alignright alignjustify | bullist numlist outdent indent | " +
                    "removeformat",
                  content_style:
                    "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
                  file_picker_callback: (cb, value, meta) => {
                    const input = document.createElement("input");
                    input.setAttribute("type", "file");
                    input.setAttribute("accept", "image/*");

                    input.addEventListener("change", (e) => {
                      const file = e.target.files[0];

                      const reader = new FileReader();
                      reader.addEventListener("load", () => {
                        /*
                            Note: Now we need to register the blob in TinyMCEs image blob
                            registry. In the next release this part hopefully won't be
                            necessary, as we are looking to handle it internally.
                          */
                        const id = "blobid" + new Date().getTime();
                        const blobCache =
                          tinymce.activeEditor.editorUpload.blobCache;
                        const base64 = reader.result.split(",")[1];
                        const blobInfo = blobCache.create(id, file, base64);
                        blobCache.add(blobInfo);

                        /* call the callback and populate the Title field with the file name */
                        cb(blobInfo.blobUri(), { title: file.name });
                      });
                      reader.readAsDataURL(file);
                    });

                    input.click();
                  },
                }}
              />
            </div>
          </div>
        </Paper>
      </Box>
      {/* action btn */}
      <div className="action-area">
        <IconButton color="success">
          <CheckCircleRoundedIcon sx={{ fontSize: 60 }} />
        </IconButton>
        <IconButton color="warning">
          <CancelIcon sx={{ fontSize: 60 }} />
        </IconButton>
      </div>
    </div>
  );
};

export default CreatPost;
