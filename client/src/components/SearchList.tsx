import React from "react";
import { SearchResult } from "../model";
import TextAnimation from "./animations/TextAnimation";
import UrlList from "./UrlList";

interface Props {
  searchResult: SearchResult | undefined;
}

let getSearchTerm = (searchResult: SearchResult | undefined) => {
  if (searchResult) {
    return searchResult.searchTerm;
  } else {
    return "";
  }
};

let getMessage = (searchResult: SearchResult | undefined) => {
  if (searchResult) {
    return searchResult.message;
  } else {
    return "";
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
    <div className="search-list m-5 text-center">
      <h2 className="m-3">{getSearchTerm(searchResult)}</h2>
      <TextAnimation message={getMessage(searchResult)} />
      <div className="m-3">{getSearchUrls(searchResult)}</div>
    </div>
  );
};

export default SearchList;
