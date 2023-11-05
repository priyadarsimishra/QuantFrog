import * as React from 'react';
import Logo from "../images/logo.png";
import GG from "../images/gg.png";
import search from "../images/search.png";
import G2 from "../images/group2.png";

const Home = () => {

    return (
        <div>
            <div className="bg-[#1f1f22] py-3.5">
                <img src={Logo} className="h-6 mx-auto bg-[#1f1f22]"/>
            </div>
            <div className="bg-[#5C5C62] h-0.5"/>

            <div className="mt-12 mb-30 flex">
                <img src={GG} className="h-80 ml-20"/>
                <img src={G2} className="h-[612px] mr-auto"/>
            </div>

            <div className='mt-[-200px] flex'>

                <input className='search' placeholder='Search a Ticker'></input>
                <button className="button"> <img src={search} className="srch"/></button>

            </div>

            <div className="bg-[#5C5C62] h-0.5"/>
            <div className="bg-[#1f1f22] py-6">
            </div>
        </div>
    )
}
export default Home;  