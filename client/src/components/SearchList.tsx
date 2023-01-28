import React from "react";
import { SearchResult } from "../model";
import UrlList from "./UrlList";

interface Props {
  searchResult: SearchResult | undefined;
}

let getSearchTerm = (searchResult: SearchResult | undefined) => {
  if (searchResult) {
    return searchResult.searchTerm;
  } else {
    return "Hello there!";
  }
};

let getMessage = (searchResult: SearchResult | undefined) => {
  if (searchResult) {
    return searchResult.message;
  } else {
    return "Search for something above and I can give you an answer.";
  }
};

let getSearchUrls = (searchResult: SearchResult | undefined) => {
  if (searchResult) {
    return <UrlList urls={searchResult.urls} />;
  } else {
    return [];
  }
};

const SearchList: React.FC<Props> = ({ searchResult }) => {
  return (
    <div className="border border-dark m-5 text-center">
      <h2 className="m-3">{getSearchTerm(searchResult)}</h2>
      <p className="m-3">{getMessage(searchResult)}</p>
      <div className="m-3">{getSearchUrls(searchResult)}</div>
    </div>
  );
};

export default SearchList;
