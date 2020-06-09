import React from "react"
import NavbarTiles from "./NavbarTiles"

const Navbar = () => {
    return(
        <div>
            <ul>
                <NavbarTiles chore="Home" />
                <NavbarTiles chore="About" />
                <NavbarTiles chore="Services" />
                <NavbarTiles chore="Contact Us!" />
                <NavbarTiles chore="Login" />
            </ul>
        </div>
    );
}

export default Navbar;