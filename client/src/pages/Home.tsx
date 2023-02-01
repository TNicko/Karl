import React from "react";
import TitleAnimation from "../components/animations/TitleAnimation";
import SearchBar from "../components/SearchBar";
import SearchList from "../components/SearchList";
import { SearchResult } from "../model";

interface State {
  searchTerm: string;
  searchResult: SearchResult | undefined;
  crawlingStatus: string | null;
  taskId: string | null;
  sessionId: string | null;
}

class Home extends React.Component {
  state: State = {
    searchTerm: "",
    searchResult: undefined,
    crawlingStatus: null,
    taskId: null,
    sessionId: null,
  };
  statusInterval: NodeJS.Timer = setInterval(() => {}, 0);

  handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (this.state.searchTerm) {
      let response = await fetch(
        `http://localhost:8000/api/search/?q=${this.state.searchTerm}`,
        {
          method: "POST",
        }
      );
      let data = await response.json();
      this.setState(
        {
          taskId: data.task_id,
          crawlingStatus: data.status,
          sessionId: data.session_id,
        },
        () => {
          this.statusInterval = setInterval(this.checkCrawlingStatus, 2000);
        }
      );
    }
  };

  checkCrawlingStatus = async () => {
    if (this.state.taskId) {
      let response = await fetch(
        `http://localhost:8000/api/search/?task_id=${this.state.taskId}`,
        {
          method: "GET",
        }
      );
      let data = await response.json();
      this.setState({
        crawlingStatus: data.status,
      });
      if (data.status === "finished") {
        this.setState({
          searchResult: data.content,
        });
      }
    }
  };

  render() {
    return (
      <div className=" my-5 d-flex flex-column align-items-center">
        <div className="d-flex align-items-center">
          <span className="title font-weight-bold">
            <TitleAnimation />
          </span>
        </div>
        <SearchBar
          searchTerm={this.state.searchTerm}
          handleSearch={this.handleSearch}
          setSearchTerm={(searchTerm) => this.setState({ searchTerm })}
        />
        <SearchList searchResult={this.state.searchResult} />
      </div>
    );
  }
}

export default Home;
