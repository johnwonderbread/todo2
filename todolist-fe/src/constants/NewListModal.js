import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewListForm from "./NewListForm";

class NewListModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Editing List";
    var button = <Button onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Creating New List";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewListForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              list={this.props.list}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewListModal;
