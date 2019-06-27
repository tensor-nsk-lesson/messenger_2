import React from 'react';
import './register.css'
import {NavLink} from "react-router-dom";

export default class RegisterForm extends React.Component {


    render() {
        return (
            <form className="form" action="">
                <input
                       className="form__input"
                       placeholder="Имя"
                       type="text"
                />
                <input
                       className="form__input"
                       placeholder="Номер телефона"
                       type="number"
                />
                <input
                       className="form__input"
                       placeholder="Пароль"
                       type="password"
                />
                <NavLink className="form__register-button" to="/profile">
                    зарегистрироваться
                </NavLink>
                <NavLink className="form__login-button" to="/login">
                    войти
                </NavLink>
            </form>
        )
    }
}
