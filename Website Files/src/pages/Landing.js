import React from 'react';
//import Started from './components/Started';
import Menubar from '../components/Menubar';
import Header from '../components/Header';
import About from '../components/About';
import Howitworks from '../components/Howitworks';
import Getstarted from '../components/Getstarted';
import Startedmodal from '../components/Startedmodal';
import Categories from '../components/Categories';
import Team from '../components/Team';
import Contact from '../components/Contact';
import Footer from '../components/Footer';
//import Home from './pages/Home';
//import Startfundraiser from './Startfundraiser';
//import Signup from './Signup';





class Landing extends React.Component {
  

  render(){
  
  return (

    <div className="landing">
        
        
            <Menubar></Menubar>
        

            {/* Header section*/}
            <Header></Header>


            {/* About Us section*/}
            <About></About>





            {/* Why Raabta section*/}  
            {/*  
                <div id="why-raabta" class="clearfix">
                    <div class="container" id="why-raabta-Container">
                        <header class="page-header colorA2">
                            <h2 className="section-heading">Why Raabta</h2>
                        </header>
                    <div class="row">
                        <div class="why-raabta-divs col-4 col-m-6 col-m2-12">
                            <img src="img/1.jpeg" alt="brand-teams" />
                            <div class="why-raabta-content">
                                <h5 class="colorA1">Split Costs</h5>
                                <p class="colorA2 section-subheading">Riders contribute an amount based on distance.</p>
                            </div>
                        </div>
                        
                        <div class="why-raabta-divs col-4 col-m-6 col-m2-12">
                            <img src="img/2.jpeg" alt="market-teams" />
                            <div class="why-raabta-content">
                                <h5 class="colorA1">Connect</h5>
                                <p class="colorA2 section-subheading">Living in the city can be a social experience.</p>
                            </div>
                        </div>
                        
                        <div class="why-raabta-divs col-4 col-m-6 col-m2-12" id="why-raabta-div-3">
                            <img src="img/3.jpeg" alt="sales-teams" />
                            <div class="why-raabta-content">
                                <h5 class="colorA1">Reduce Congestion</h5>
                                <p class="colorA2 section-subheading">Help reduce the number of cars on the roads.</p>
                            </div>
                        </div>
                    </div> 
                        
                    </div>
            </div> */}


            {/* How it works section*/}   
                <Howitworks></Howitworks>


            {/* Get started Grid */} 
            <Getstarted></Getstarted>

            


            {/* Started Grid 
            <Started startedLinks={startedLinks}></Started> */}
            

            <Startedmodal></Startedmodal>
            
            {/* Categories */}
            <Categories></Categories>


            {/* Team */}
            <Team></Team>

            
            
            {/* Contact */}
            <Contact></Contact>

            {/* Footer */}
            <Footer></Footer>
    </div>

  
        
  );
  }
}

export default Landing;
