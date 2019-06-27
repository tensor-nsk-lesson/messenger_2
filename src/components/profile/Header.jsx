import React from "react";


class Header extends React.Component{
    constructor(props){
        super(props);
        this.name = props.name;
        this.isOnline = props.isOnline;
    }
    render(){
        return(
            <div className="profile__info__header">
                <h1>
                    Алексей
                    {this.name}
                </h1>
                <h2>
                    +79528074028
                    {this.number}
                </h2>
                <h3>В сети{this.isOnline}</h3>
            </div>
        );
    }
}


export default Header;