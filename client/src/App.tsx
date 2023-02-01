import React from "react";
import "./App.css";
import { DefaultDark, Theme } from "./ThemeContext";
import useLocalStorage from "use-local-storage";
import Navbar from "./components/Navbar";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";

const App: React.FC = () => {
  const [theme, setTheme] = useLocalStorage<Theme>(
    "theme",
    DefaultDark ? Theme.dark : Theme.light
  );

  const toggleTheme = () => {
    setTheme((curr) => (curr === Theme.light ? Theme.dark : Theme.light));
  };

  return (
    <div className="App" data-theme={theme}>
      <Navbar theme={theme} toggleTheme={toggleTheme} />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
};

export default App;
