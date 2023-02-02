import React from "react";
import { SearchData } from "../model";
import TextAnimation from "./animations/TextAnimation";
import UrlList from "./UrlList";

interface Props {
  searchData: SearchData | undefined;
}

let getSearchTerm = (searchData: SearchData | undefined) => {
  if (searchData) {
    return searchData.searchTerm;
  } else {
    return "";
  }
};

let getMessage = (searchData: SearchData | undefined) => {
  if (searchData) {
    return searchData.message;
  } else {
    return "";
  }
};

let getSearchUrls = (searchData: SearchData | undefined) => {
  if (searchData) {
    return <UrlList urls={searchData.urls} />;
  } else {
    return [];
  }
};

const SearchList: React.FC<Props> = ({ searchData }) => {
  return (
    <div className="search-list m-5 text-center">
      <h2 className="m-3">{getSearchTerm(searchData)}</h2>
      <TextAnimation message={getMessage(searchData)} />
      <div className="m-3">{getSearchUrls(searchData)}</div>
    </div>
  );
};

export default SearchList;
