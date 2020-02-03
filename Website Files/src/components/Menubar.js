import React from 'react';
import {FaAlignRight} from 'react-icons/fa';
import { Link } from 'react-router-dom';
import Signup from '../pages/Signup';

class Menubar extends React.Component{

  state = {isOpen:false}
  handleToggle = () =>{
    this.setState({isOpen: !this.state.isOpen})

  }

  


    render(){

       return (

        <nav className="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
        <div className="container">
          <a className="navbar-brand js-scroll-trigger" href="#page-top">Raabta</a>
          <button className="navbar-toggler navbar-toggler-right" type="button"  data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation" onClick={this.handleToggle}>
  
            <FaAlignRight className="nav-icon"></FaAlignRight>
          </button>
          <div className="collapse navbar-collapse" id="navbarResponsive">
          <ul className="navbar-nav text-uppercase ml-auto">
              <li className="nav-item">
                <a className="nav-link js-scroll-trigger" href="#aboutus">About us</a>
              </li>
              <li className="nav-item">
                <a className="nav-link js-scroll-trigger" href="#started">Get Started</a>
              </li>
              <li className="nav-item">
                <a className="nav-link js-scroll-trigger" href="#categories">Categories</a>
              </li>
              <li className="nav-item">
                <a className="nav-link js-scroll-trigger" href="#team">Team</a>
              </li>
              <li className="nav-item">
                <a className="nav-link js-scroll-trigger" href="#contact">Contact</a>
              </li>
              
              <li className="nav-item">
                <Link className="nav-link js-scroll-trigger" to="/signup">Login / Register</Link>
              </li>
            
            </ul>
           
          </div>
         
        </div>
      </nav>



       );

    }
}


export default Menubar;