import React from "react";
import { ThemeSwitch, Theme } from "../ThemeContext";
import AppsIcon from "@mui/icons-material/Apps";

interface Props {
  theme: Theme;
  toggleTheme: () => void;
}

const Navbar: React.FC<Props> = ({ theme, toggleTheme }) => {
  return (
    <div
      className="navbar container-fluid py-2 px-3"
      style={{
        color: "var(--text-secondary)",
        borderBottom: "1px solid var(--border-primary)",
      }}
    >
      <AppsIcon />
      <ThemeSwitch
        sx={{ m: 1 }}
        checked={theme === Theme.dark}
        onChange={toggleTheme}
      />
    </div>
  );
};

export default Navbar;
