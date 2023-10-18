import { Dialog, DialogTitle } from "@mui/material";
import { CancelOutlined as CancelOutlinedIcon } from "@mui/icons-material";
import { useState } from "react";

const BaseDialog = (props) => {
  const { onClose, open, title } = props;

  const handleClose = () => {
    onClose();
  };

  return (
    <Dialog onClose={handleClose} open={open} {...props}>
      <DialogTitle
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        {title}
        <CancelOutlinedIcon sx={{ cursor: "pointer" }} onClick={handleClose} />
      </DialogTitle>
      {props.children}
    </Dialog>
  );
};

export default BaseDialog;
