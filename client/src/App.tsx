import React, { useState } from "react";
import "./App.css";
import SearchBar from "./components/SearchBar";
import SearchList from "./components/SearchList";
import { SearchResult } from "./model";
import { DefaultDark, Theme } from "./ThemeContext";
import useLocalStorage from "use-local-storage";
import Navbar from "./components/Navbar";
import TitleAnimation from "./components/animations/TitleAnimation";

const App: React.FC = () => {
  const [theme, setTheme] = useLocalStorage<Theme>(
    "theme",
    DefaultDark ? Theme.dark : Theme.light
  );

  const [searchTerm, setSearchTerm] = useState<string>("");
  const [searchResult, setSearchResult] = useState<SearchResult | undefined>(
    undefined
  );

  const toggleTheme = () => {
    setTheme((curr) => (curr === Theme.light ? Theme.dark : Theme.light));
  };

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log("searchTerm: ", searchTerm);

    if (searchTerm) {
      let response = await fetch(
        `http://localhost:8000/api/search/?q=${searchTerm}`
      );
      let data = await response.json();
      setSearchResult(data);
    }
  };

  return (
    <div className="App" data-theme={theme}>
      <Navbar theme={theme} toggleTheme={toggleTheme} />
      <div className="mt-5 d-flex align-items-center">
        <span className="title font-weight-bold">
          <TitleAnimation />
        </span>
      </div>
      <SearchBar
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        handleAdd={handleAdd}
      />
      <SearchList searchResult={searchResult} />
    </div>
  );
};

export default App;
