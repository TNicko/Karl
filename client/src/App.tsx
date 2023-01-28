import React, { useState } from "react";
import "./App.css";
import SearchBar from "./components/SearchBar";
import SearchList from "./components/SearchList";
import { SearchResult } from "./model";

const App: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [searchResult, setSearchResult] = useState<SearchResult | undefined>(
    undefined
  );

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();

    if (searchTerm) {
      let response = await fetch(
        `http://localhost:8000/api/search/?q=${searchTerm}`
      );
      let data = await response.json();
      setSearchResult(data);
    }
  };

  return (
    <div className="App">
      <span className="heading font-weight-bold">K A R L</span>
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
