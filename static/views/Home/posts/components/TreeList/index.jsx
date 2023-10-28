import "./index.scss";
import { useState } from "react";
import {
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Typography,
} from "@mui/material";
import {
  ExpandMore as ExpandMoreIcon,
  Aod as AodIcon,
  AssistantOutlined as AssistantOutlinedIcon,
  AttachMoneyOutlined as AttachMoneyOutlinedIcon,
} from "@mui/icons-material";

const TreeList = () => {
  return (
    <div className="left-tree">
      <Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography>Accordion 1</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <AodIcon /> content 1
        </AccordionDetails>
        <AccordionDetails>
          <AodIcon /> content 1
        </AccordionDetails>
        <AccordionDetails>
          <AodIcon /> content 1
        </AccordionDetails>
      </Accordion>
      <Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel2a-content"
          id="panel2a-header"
        >
          <Typography>Accordion 2</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <AssistantOutlinedIcon />
          menu 2
        </AccordionDetails>
        <AccordionDetails>
          <AssistantOutlinedIcon />
          menu 2
        </AccordionDetails>
        <AccordionDetails>
          <AssistantOutlinedIcon />
          menu 2
        </AccordionDetails>
        <AccordionDetails>
          <AssistantOutlinedIcon />
          menu 2
        </AccordionDetails>
      </Accordion>
      <Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel3a-content"
          id="panel3a-header"
        >
          <Typography> Accordion 3</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <AttachMoneyOutlinedIcon />
          Accordion 3
        </AccordionDetails>
        <AccordionDetails>
          <AttachMoneyOutlinedIcon />
          Accordion 3
        </AccordionDetails>
        <AccordionDetails>
          <AttachMoneyOutlinedIcon />
          Accordion 3
        </AccordionDetails>
      </Accordion>
    </div>
  );
};

export default TreeList;
