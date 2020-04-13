import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import TodoList from "./TodoList";
import NewListModal from "./NewListModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    lists: []
  };

  componentDidMount() {
    this.resetState();
  }

  getLists = () => {
    axios.get(API_URL).then(res => this.setState({ lists: res.data }));
  };

  resetState = () => {
    this.getLists();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <TodoList
              lists={this.state.lists}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewListModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
