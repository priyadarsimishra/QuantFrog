import React, {useState, useEffect } from 'react';
import Logo from "../images/logo.png";
import GG from "../images/gg.png";
import search from "../images/search.png";
import G2 from "../images/group2.png";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const[ticker, setTicker] = useState("");
    const navigate = useNavigate();

    const handleSubmit = () => {
        console.log("clicked")
        if(ticker && ticker.length <= 4)
        {
            console.log("ticket: "+ ticker);
            navigate(`/stock/${ticker?.toUpperCase()}`);
        }
    }

    return (
        <div>
            <div className="bg-[#1f1f22] py-3.5 flex align-center">
                <img src={Logo} className="h-6 mx-auto bg-[#1f1f22]"/>
            </div>
            <div className="bg-[#5C5C62] h-0.5"/>

            <div className="mb-30 flex items-center">
                <img src={GG} className="h-80 ml-20"/>
                <img src={G2} className="h-[612px] mr-auto ml-auto mt-20"/>
            </div>

            <div className='mt-[-130px] flex'>

                <input 
                    className='search'
                    placeholder='Search a Ticker' 
                    type="text" 
                    name="name" 
                    value={ticker}
                    onChange={(e) => setTicker(e.target.value)}
                ></input>
                <button 
                    className="button"
                    onClick={handleSubmit}
                > <img src={search} className="srch"/></button>

            </div>

            {/* <div className="absolute inset-x-0 bottom-0 bg-[#5C5C62] h-0.5"/> */}
            <div className="absolute inset-x-0 bottom-0 bg-[#1f1f22] h-8 py-6 border-t-2 border-gray-500">
                <h3 className='flex items-center justify-center text-lime-300 text-lg font-semibold' style={{marginTop: "-15px"}}>Make Things Possible.</h3>
            </div>
        </div>
    )
}
export default Home;  