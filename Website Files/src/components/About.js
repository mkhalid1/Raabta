import React from 'react';

class About extends React.Component{


    render(){

        return (
            <section className="page-section" id="aboutus">
            <div className="container">
              <div className="row">
                <div className="col-lg-12 text-center">
                  <h2 className="section-heading">About Us</h2>
                  <h3 className="section-subheading">Connecting for better..</h3>
                </div>
              </div>
              <div className="row text-center">
                <div className="col-md-6">
                  <span className="fa-stack fa-4x">
                    <i className="fa fa-circle fa-stack-2x text-primary"></i>
                    <i className="fa fa-laptop fa-stack-1x fa-inverse"></i>
                  </span>
                  <h4 className="service-heading">Community Service Website</h4>
                  <p className="section-subheading">Web based application  where people  post about their financial needs or that of others  along with proof  and contact information. </p>
                </div>
                <div className="col-md-6">
                  <span className="fa-stack fa-4x">
                    <i className="fa fa-circle fa-stack-2x text-primary"></i>
                    <i className="fa fa-file fa-stack-1x fa-inverse"></i>
                  </span>
                  <h4 className="service-heading">Data Scraping</h4>
                  <p className="section-subheading">Application also scrapes data from social media sites where information is shared  regarding people who require urgent financial assistance.</p>
                </div>
                <div className="col-md-6">
                  <span className="fa-stack fa-4x">
                    <i className="fa fa-circle fa-stack-2x text-primary"></i>
                    <i className="fa fa-object-group fa-stack-1x fa-inverse"></i>
                  </span>
                  <h4 className="service-heading">Data Clustering</h4>
                  <p className="section-subheading">Data collected  is clustered  into different categories like education, medical, basic necessities etc.</p>
                </div>
        
                <div className="col-md-6">
                  <span className="fa-stack fa-4x">
                    <i className="fa fa-circle fa-stack-2x text-primary"></i>
                    <i className="fa fa-check-circle fa-stack-1x fa-inverse"></i>
                  </span>
                  <h4 className="service-heading">Authenticity</h4>
                  <p className="section-subheading"> Only genuine applications will be posted on the website after screening.</p>
                </div>
               
              </div>
            </div>
          </section>


        );
    }





}

export default About;