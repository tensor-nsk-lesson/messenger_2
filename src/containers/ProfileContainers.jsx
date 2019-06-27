import React from 'react';
import Header from "../components/profile/Header";
import {connect} from "react-redux";
import '../components/profile/profile.css';

class ProfileContainer extends React.Component{
    render(){
        return(
            <div className="profile">
                <div className="profile2">
                    <div className="profile__photo">
                    </div>
                    <div className="profile__info">
                        <Header name={`${this.props.profile.firstName} ${this.props.profile.number}`} isOnline={this.props.profile.isOnline}/>
                    </div>
                </div>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        profile: state.profile
    }
};


export default connect(mapStateToProps)(ProfileContainer);