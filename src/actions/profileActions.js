export const SET_FIRST_NAME = 'SET_FIRST_NAME';
export const SET_NUMBER = 'SET_NUMBER';
export const SET_PASSWORD = 'SET_PASSWORD';


export const setFirstName = firstName =>({
    type: SET_FIRST_NAME,
    payload: firstName
});

export const setNumber = Number =>({
    type: SET_NUMBER,
    payload: Number
});

export const setPassword = password =>({
    type: SET_PASSWORD,
    payload: password
});