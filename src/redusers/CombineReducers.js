import {combineReducers} from "redux";
import {profileReducer} from "./ProfileReducer";

export default combineReducers({
    profile: profileReducer
});