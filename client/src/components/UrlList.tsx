import React from "react";
import { styled } from "@mui/material/styles";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import LinkIcon from "@mui/icons-material/Link";

const ListBox = styled("div")(() => ({
  display: "flex",
  justifyContent: "center",
}));

interface Props {
  urls: string[];
}

const UrlList: React.FC<Props> = ({ urls }) => {
  return (
    <Grid item xs={12} md={6}>
      <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="div">
        References
      </Typography>
      <ListBox>
        <List>
          {urls.map((url, i) => (
            <ListItem key={i}>
              <ListItemIcon>
                <LinkIcon />
              </ListItemIcon>
              <ListItemText primary={url} />
            </ListItem>
          ))}
        </List>
      </ListBox>
    </Grid>
  );
};

export default UrlList;
