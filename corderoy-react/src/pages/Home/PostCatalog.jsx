import React from "react";
import classNames from "classnames";

export default class PostCatalog extends React.Component {
  render() {
    return (
        <div className={classNames('PostCatalog', this.props.className)}>
          
        </div>
    );
  }
}