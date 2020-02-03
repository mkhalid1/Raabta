import React from 'react';


class Howitworks extends React.Component{


    render(){

        return (

            <div id="how-it-works" class="clearfix">
            <div className="container colorA2">
                
                <div id="how-it-works-box" class="col-12 col-m-12 col-m2-12">
                    <header className="page-header">
                        <h2 className="section-heading">How It Works</h2>
                    </header>
                    
                    <div className="row how-it-works-div">
                    <div className="how-it-works-content clearfix">
                        <div className="item-image col-6">
                            <img src="img/signup.png"/>
                        </div>
                        
                        <div className="item-content col-6">
                            <h5 className="colorA1">Get Started</h5>
                            <p className="colorA2 section-subheading">Go to our website, and sign up to create an account</p>
                        </div>
                    </div>
                    </div>
                   
                    <div className="row how-it-works-div">
                    <div className="how-it-works-content clearfix">
                                            
                        <div className="item-content col-6">
                            <h5 className="colorA1">Start a fundraiser or search for a category </h5>
                            <p className="colorA2 section-subheading">Two possible ways to help those in need</p>
                        </div>
                    
                        <div className="item-image col-6">
                            <img src="img/search.png"/>
                        </div>
    
                    </div>
                    </div>
                    
                    <div className="row how-it-works-div">
                    <div className="how-it-works-content clearfix">
                        <div className="item-image col-6">
                            <img src="img/select.png"/>
                        </div>
                        
                        <div className="item-content col-6">
                            <h5 className="colorA1">Contribute to an existing fundraiser</h5>
                            <p className="colorA2 section-subheading">Select a category of your interest and choose one of the existing fundraisers in it to make your contribution</p>
                        </div>
                    </div>
                    </div>
                    
                    <div className="row how-it-works-div">
                    <div className="how-it-works-content clearfix">
                        
                        <div className="item-content col-6">
                            <h5 className="colorA1">Start a fundraiser</h5>
                            <p className="colorA2 section-subheading">Create a fundraiser on your own by providing the necessary details</p>
                        </div>
                    
                        <div className="item-image col-6">
                            <img src="img/fundraiser.png"/>
                        </div>
                    </div>
                    </div>
                    
                   
                    
                </div>
             </div>
         </div>
    

        );
    }





}

export default Howitworks;