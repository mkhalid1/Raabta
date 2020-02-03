import React from 'react';




class Categories extends React.Component{


    render(){

        return (

            <div id="categories" class="container">
                <header className="page-header">
                    <h2 className="section-heading">Browse by Category</h2>
                </header>
                <ul className="category-opt section-subheading">
                    <li> <a href="#basicneeds"> <i className="fa fa-home"></i> Basic Needs</a></li>
                    <li><a href="#medical"> <i className="fa fa-wheelchair"></i>  Medical</a></li>
                    <li ><a href="#education"> <i className="fa fa-graduation-cap"></i> Education</a></li>
                    <li ><a href="#animals"> <i className="fa fa-paw"></i> Animals & Pets</a></li>  
                    <li ><a href="#loans"> <i className="fa fa-money"></i>  Loans</a></li>
                    <li ><a href="#bills"> <i className="fa fa-credit-card"></i> Bills</a></li>
                    <li ><a href="#misc"> <i className="fa fa-plus"></i> Miscellaneous</a></li>
                </ul>
            </div>

        );
    }





}

export default Categories;