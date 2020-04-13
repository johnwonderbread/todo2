import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewListForm extends React.Component {
  state = {
    id: 0,
    user: "",
    item: "",
    duedate: "",
  };

  componentDidMount() {
    if (this.props.list) {
      const { id, user, item, duedate} = this.props.list;
      this.setState({ id, user, item, duedate});
    }
  }

  onChange = e => {
    console.log(e)
    this.setState({ [e.target.name]: e.target.value });
  };

  createList = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editList = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.id, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.list ? this.editList : this.createList}>
        <FormGroup>
          <Label for="item">Task:</Label>
          <Input
            type="text"
            name="item"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.item)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="duedate">Due Date:</Label>
          <Input
            type="date"
            name="duedate"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.duedate)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewListForm;
