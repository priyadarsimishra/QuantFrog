import * as React from 'react';
import Logo from "../images/logo.png";
import TVtape from "./TradingViewWidget";
import { TickerTape } from "react-ts-tradingview-widgets";
import { TechnicalAnalysis } from "react-ts-tradingview-widgets";
import { Timeline } from "react-ts-tradingview-widgets";
import { useParams } from 'react-router-dom';

const Stock = () => {
    let { ticker } = useParams();

    return (
        <div>
            <div className="bg-[#1f1f22] py-3.5">
                <img src={Logo} className="h-6 mx-auto bg-[#1f1f22]"/>
            </div>
            <div className="bg-[#5C5C62] h-0.5"/>

            <div className='tape'>
                <TickerTape colorTheme="dark"></TickerTape>
            </div>

            <div className='fx'>
                <div className="tvw">
                    <TVtape ticker={ticker}/>
                </div>

                <div className='tech'>
                    <div className="tvtech">
                        <TechnicalAnalysis symbol={ticker} className="gg" colorTheme="dark" width="100%"></TechnicalAnalysis>
                    </div>
                </div>
            </div>

            <div className='time'>
                <Timeline colorTheme="dark" feedMode="market" market="stock" height={400} width="100%"></Timeline>
            </div>

        </div>
    )
}

export default Stock;