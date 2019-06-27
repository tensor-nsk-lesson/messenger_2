import React from 'react';
import {connect} from "react-redux";
import {Route, BrowserRouter} from 'react-router-dom';
import Register from "./containers/RegisterContainers";
import Sidebar from './components/sidebar/sidebar';
import ProfileContainer from "./containers/ProfileContainers";


class App extends React.Component {
    render() {
        const WrapperRegister = () => {
            return (<Register isLogin="0"/>)
        };
        const WrapperLogin = () => {
            return (<Register isLogin="1"/>)
        };
        return (
            <BrowserRouter>
                {this.props.profile.auth === 1 ? (
                    <div>
                        <Route path="/register" component={WrapperRegister}/>
                        <Route path="/login" component={WrapperLogin}/>
                    </div>
                ):(
                    <div className="main">
                        <Sidebar />
                        <div className="main__content">
                            <Route exact path="/profile" component={ProfileContainer}/>
                            <Route exact path="/dialogs" component={ProfileContainer}/>
                            <Route exact path="/settings" component={ProfileContainer}/>
                            <Route exact path="/exit" component={ProfileContainer}/>
                        </div>
                    </div>
                )
                }
            </BrowserRouter>
        );
    }
}

const mapStateToProps = store => {
    return {
        profile: store.profile,
    }
};

export default connect(mapStateToProps)(App);