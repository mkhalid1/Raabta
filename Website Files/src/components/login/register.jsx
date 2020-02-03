import React from "react";
import loginImg from "../../login.svg";
import { BrowserRouter as Router, Route, Switch, Link, Redirect } from 'react-router-dom';

export class Register extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="base-container" ref={this.props.containerRef}>
        <div className="header">Register</div>
        <div className="content">
          <div className="image">
            <img src={loginImg} />
          </div>
          <div className="form">
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input type="text" name="username" placeholder="Your name" />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="email" name="email" placeholder="Your email" />
            </div>
        
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input type="password" name="password" placeholder="Your password" />
            </div>
          </div>
        </div>
        <div className="footer">
          <Link to="/"><button type="button" className="login-btn">
            Register
          </button> </Link>
        </div>
      </div>
    );
  }
}
