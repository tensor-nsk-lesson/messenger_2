import {
    SET_FIRST_NAME,
    SET_NUMBER,
    SET_PASSWORD,
} from "../actions/profileActions";

const defaultState = {
    auth: 0,
    firstName: '',
    number: '',
    password: '',
    isOnline: '',
};

export const profileReducer = (state = defaultState, action) => {
    switch (action.type) {
        case SET_FIRST_NAME:
            return {
                ...state,
                firstName: action.payload
            };
        case SET_NUMBER:
            return {
                ...state,
                number: action.payload
            };
        case SET_PASSWORD:
            return {
                ...state,
                password: action.payload
            };
    }
    return state
};