import React from 'react';
import '../components/Auth/register.css'
import {LoginForm} from "../components/Auth/LoginForm";
import {setFirstName, setNumber, setPassword} from "../actions/profileActions";
import {connect} from "react-redux";
import RegisterForm from "../components/Auth/RegisterForm";

class RegisterContainer extends React.Component {
    render() {
        return (
            <div className="main__reg">
                <div className="main__leftSide"/>
                <div className="main__rightSide">
                    <h1 className="head">Регистрация</h1>
                    {this.props.isLogin === 1 ? (
                        <RegisterForm


                        />
                    ) : (
                        <LoginForm/>
                    )
                    }
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        firstName: state.profile.firstName,
        email: state.profile.email,
        password: state.profile.password,
        isOnline: state.profile.isOnline,
    }
};

const mapDispatchToProps = {
    setFirstName,
    setNumber,
    setPassword
};


export default connect(mapStateToProps, mapDispatchToProps)(RegisterContainer);