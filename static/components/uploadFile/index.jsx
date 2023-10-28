import React, { useState } from "react";
import {
  Button,
  Typography,
  Paper,
  CircularProgress,
  Box,
} from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

const FileUpload = (props) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (selectedFile) {
      // You can perform the file upload here
      // Typically, you would make an HTTP request to a server to handle the upload
      // For simplicity, we'll just simulate the upload with a timeout
      setUploading(true);

      setTimeout(() => {
        setUploading(false);
        alert("File uploaded successfully!");
      }, 2000);
    } else {
      alert("Please select a file to upload.");
    }
  };

  return (
    <div {...props}>
      <Paper elevation={3} style={{ width: "100%" }}>
        <div style={{ padding: "20px" }}>
          <Typography variant="h6" gutterBottom>
            File Upload
          </Typography>
          <input
            type="file"
            accept=".jpg, .png, .jpeg, .gif"
            style={{ display: "none" }}
            id="file-input"
            onChange={handleFileChange}
          />
          <label htmlFor="file-input">
            <Button
              variant="contained"
              component="span"
              startIcon={<CloudUploadIcon />}
            >
              Select File
            </Button>
          </label>
          <Typography variant="body1" style={{ marginTop: "16px" }}>
            {selectedFile ? selectedFile.name : "No file selected"}
          </Typography>
          <Box mt={2}>
            <Button
              variant="contained"
              color="primary"
              onClick={handleUpload}
              disabled={uploading}
            >
              Upload
            </Button>
          </Box>
          {uploading && (
            <Box mt={2} display="flex" justifyContent="center">
              <CircularProgress />
            </Box>
          )}
        </div>
      </Paper>
    </div>
  );
};

export default FileUpload;
