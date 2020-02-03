import React from 'react'

export default ({ startedLinks }) => {
    return (

    <section className="bg-light page-section" id="started">
      <div className="container">
        <div className="row">
          <div className="col-lg-12 text-center">
            <h2 className="section-heading ">Ideas To Get You Started</h2>
            <h3 className="section-subheading">There are a lot of ways to make good things happen...</h3>
          </div>
        </div>
        <div className="row">
          {
            startedLinks && startedLinks.map(({title,caption,source},index)=>

            <div className="col-md-6 col-sm-12 started-item">
                <a className="started-link" data-toggle="modal" href="#startedModal1">
                  <div className="started-hover">
                    <div className="started-hover-content">
                      <i className="fa fa-plus fa-3x"></i>
                    </div>
                  </div>
                  <img className="img-fluid" src= { source } alt=""/>
                </a>
                <div className="started-caption">
                  <h4>{title}</h4>
                  <p className="section-subheading">{caption}</p>
                  <p><a className=" btn btn-primary btn-xl text-uppercase js-scroll-trigger">Start Fundraising</a></p>
                </div>
                
                
                
          </div>
          

            )
          
          }
        </div>
       
      </div>
      
  </section>


        
    );
}