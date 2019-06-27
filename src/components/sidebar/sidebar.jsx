import React from 'react';
import './sidebar.css'
import SidebarNavItem from "./sidebarNavItem";

class Sidebar extends React.Component {
    render() {
        return (
            <div className="main__navBar">
                <div className="main__navBar__items">
                    <SidebarNavItem url="/profile" img={require("../../img/profile.png")}/>
                    <SidebarNavItem url="/dialogs" img={require("../../img/messages.png")}/>
                    <SidebarNavItem url="/settings" img={require("../../img/settings.png")}/>
                    <SidebarNavItem url="/exit" img={require("../../img/exit.png")}/>
                </div>
            </div>
        );
    }
}

export default Sidebar;