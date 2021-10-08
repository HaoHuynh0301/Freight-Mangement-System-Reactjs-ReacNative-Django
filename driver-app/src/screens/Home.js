import React, { Component } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import *  as ReactBoostrap from 'react-bootstrap';
import './css/homeStyle.css';
import {
    backgroundImage,
    orangeColor,
    whiteColor
} from '../contants';
import {
    DoubleNavigationPage,
    Orders,
    MyOrders,
    Dashboard
} from './components';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from "react-router-dom";
import User from './User';
import PullToRefresh from 'react-simple-pull-to-refresh';

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            totalUrOrders: 0,
            instanceOrders: [],
            comp: ''
        }
        this.onRefresh = this.onRefresh.bind(this);
    }

    onRefresh() {
        
    }
    
    componentDidUpdate() {
        
    }

    componentDidMount() {
        this.setState({
            comp: this.props.comp
        });
    }

    mainView = (comp) => {
        if(comp === 'my-orders') {
            this.setState({
                comp: comp
            });
            return(
                <MyOrders />
            );
        }
        else if(comp === 'orders') {
            this.setState({
                comp: comp
            });
            return(
                <Orders />
            );
        } else if(comp === 'dashboard') {
            return(
                <Dashboard />
            );
            
        }
    }

    render() {
        console.log(this.state.comp);
        
        if(!this.props.isAuth) {
            return (
                <Route>
                    <Redirect to = '/sign-in'/>
                </Route>
            );
        } 
        return(
            <Router>
                <div style = {{
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center",
                }}>
                    <div style = {{
                        width: '100%',
                        height: '500px'
                    }}>
                        <DoubleNavigationPage />
                        <PullToRefresh onRefresh={this.onRefresh}>
                            {this.mainView(this.state.comp)}
                        </PullToRefresh>    
                    </div>
                </div>        
            </Router>
            
        );
    }
}

export default Home;