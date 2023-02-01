import React from "react";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";

interface Props {
  searchTerm: string;
  setSearchTerm: React.Dispatch<React.SetStateAction<string>>;
  handleSearch: (e: React.FormEvent) => void;
}

const SearchBar: React.FC<Props> = ({
  searchTerm,
  setSearchTerm,
  handleSearch,
}) => {
  return (
    <Paper
      component="form"
      onSubmit={handleSearch}
      sx={{
        backgroundColor: "var(--input-primary)",
        p: "2px 4px",
        display: "flex",
        alignItems: "center",
        width: 400,
        borderRadius: 10,
      }}
    >
      <InputBase
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        sx={{ color: "var(--text-primary)", padding: 1, ml: 1, flex: 1 }}
        placeholder="Search"
        inputProps={{ "aria-label": "search" }}
      />
      <Divider
        sx={{ borderColor: "var(--text-primary)", height: 28, m: 0.5 }}
        orientation="vertical"
      />
      <IconButton
        type="button"
        sx={{ color: "var(--text-primary)", p: "10px" }}
        aria-label="search"
        onClick={handleSearch}
      >
        <SearchIcon />
      </IconButton>
    </Paper>
  );
};

export default SearchBar;
