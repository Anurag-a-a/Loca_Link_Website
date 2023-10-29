/**
 * Top Navbar
 */
import "./index.scss";
import {
  Popover,
  Button,
  List,
  ListItem,
  Box,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  FormControl,
  InputLabel,
  OutlinedInput,
  InputAdornment,
  IconButton,
  Divider,
  Tooltip,
} from "@mui/material";
import {
  MoreHoriz,
  Inbox as InboxIcon,
  Visibility,
  VisibilityOff,
  Add as AddIcon,
  AccountBalance as AccountBalanceIcon,
  SearchOutlined as SearchOutlinedIcon,
  HighlightOffOutlined as HighlightOffOutlinedIcon,
  AddHomeWorkOutlined as AddHomeWorkOutlinedIcon,
} from "@mui/icons-material";
import BaseDialog from "@/components/dialogCommon/index.jsx";

import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const [dialogVisible, setDialogVisible] = useState(false);
  const open = Boolean(anchorEl);
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const btnMore = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const dialogClose = () => {
    setDialogVisible(false);
  };

  const btnSignUp = () => {
    setDialogVisible(true);
  };
  return (
    <>
      <div className="navbar">
        <div className="left-logo" onClick={() => navigate("/")}>
          <AccountBalanceIcon sx={{ color: "#ff4500" }} />
          &nbsp; Community
        </div>
        <div className="search">
          <SearchOutlinedIcon />
          <input className="input" placeholder="search article" />
          <HighlightOffOutlinedIcon />
        </div>

        {/* operation area */}
        <div className="right">
          <Tooltip title="create community">
            <IconButton onClick={() => navigate("/home/createCommunity")}>
              <AddHomeWorkOutlinedIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="creat post">
            <IconButton onClick={() => navigate("/home/createPost")}>
              <AddIcon />
            </IconButton>
          </Tooltip>
          &nbsp;
          <Button variant="contained" color="warning">
            Log In
          </Button>
          &nbsp;
          <div className="more-icon">
            <MoreHoriz onClick={btnMore} />
            <Popover
              open={open}
              anchorEl={anchorEl}
              onClose={handleClose}
              anchorOrigin={{
                vertical: "bottom",
                horizontal: "right",
              }}
            >
              <Box
                sx={{
                  width: "100%",
                  maxWidth: 360,
                  bgcolor: "background.paper",
                }}
              >
                <List>
                  <ListItem disablePadding onClick={btnSignUp}>
                    <ListItemButton>
                      <ListItemIcon>
                        <InboxIcon />
                      </ListItemIcon>
                      <ListItemText primary="Sign Up" />
                    </ListItemButton>
                  </ListItem>
                </List>
              </Box>
            </Popover>
          </div>
        </div>
      </div>
      <BaseDialog
        title="Sign Up"
        className="sign-form"
        open={dialogVisible}
        onClose={dialogClose}
      >
        <div className="form-main">
          <FormControl sx={{ m: 1, width: "35ch" }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Email</InputLabel>
            <OutlinedInput label="Email" />
          </FormControl>
          <FormControl sx={{ m: 1, width: "35ch" }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Name</InputLabel>
            <OutlinedInput label="Name" />
          </FormControl>
          <FormControl sx={{ m: 1, width: "35ch" }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">
              Password
            </InputLabel>
            <OutlinedInput
              id="outlined-adornment-password"
              type={showPassword ? "text" : "password"}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={() => setShowPassword((show) => !show)}
                    onMouseDown={(e) => e.preventDefault()}
                    edge="end"
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
              label="Password"
            />
          </FormControl>
        </div>
        <div className="form-footer">
          <Divider />
          <Button variant="contained" color="warning" size="large">
            Sign In
          </Button>
        </div>
      </BaseDialog>
    </>
  );
};

export default Navbar;
