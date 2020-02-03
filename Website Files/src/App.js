import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link, Redirect } from 'react-router-dom';
import Menubar from './components/Menubar';
import Landing from './pages/Landing';
import Startfundraiser from './pages/Startfundraiser';
import Signup from './pages/Signup';







class App extends React.Component {
  constructor(props){
    super(props);
   
  }

  render(){
  
  return (

    <div className="App">

        <>
         {/* Menu bar */}
         

        <Switch>

            <Route exact path="/" component ={Landing}></Route>
            
            <Route exact path="/startfundraiser" component ={Startfundraiser}></Route>
            
            <Route exact path="/signup" component ={Signup}></Route>

        </Switch>
    
        </>
        
    
   
          
        
    </div>

  
        
  );
  }
}

export default App;
