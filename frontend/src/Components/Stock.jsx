import * as React from 'react';
import Logo from "../images/logo.png";
import TVtape from "./TradingViewWidget";
import { TickerTape } from "react-ts-tradingview-widgets";
import { TechnicalAnalysis } from "react-ts-tradingview-widgets";
import { Timeline } from "react-ts-tradingview-widgets";
import Stars from "../images/stars.png"

const Stock = () => {
    return (
        <div>
            <div className="bg-[#1f1f22] py-3.5">
                <img src={Logo} className="h-6 mx-auto bg-[#1f1f22]"/>
            </div>
            <div className="bg-[#5C5C62] h-0.5"/>

            <div className='tape'>
                <TickerTape colorTheme="dark"></TickerTape>
            </div>

            <div className='flex'>
            <img src={Stars} className='h-56 ml-7 mt-11'/>
            <div className="eps">
                <div className='q1q2'>
                    <div className='q1'> 
                        <h1 className="py-8 pl-5 pr-5 text-2xl font-medium text-white">Q2</h1> 
                        <div className='divider'/>
                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Estimated EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/>

                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Reported EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/>

                        <h1 className='text-[#C2F23B] text-lg my-6 py-2 ml-6 mr-3'>value</h1>
                        
                    </div>
                    <div className='q2'>
                        <h1 className="py-8 pl-4 pr-5 text-2xl font-medium text-white">Q3</h1> 
                        <div className='divider'/>
                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Estimated EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/>

                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Reported EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/>

                        <h1 className='text-[#C2F23B] text-lg my-6 py-2 ml-6 mr-3'>value</h1>
                    </div>
                </div>
                <div className='q3q4'>
                    <div className='q3'>
                        <h1 className="py-8 pl-4 pr-5 text-2xl font-medium text-white">Q4</h1> 
                        <div className='divider'/>
                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Estimated EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/>

                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Reported EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3 px-3'>—</h1>
                        <div className='divider'/>

                        <h1 className='text-[#b5f2ed] text-lg my-6 py-2 ml-9 mr-3'>—</h1>
                    </div>
                    <div className='q4'>
                        <h1 className="py-8 pl-4 pr-5 text-2xl font-medium text-white">Q1</h1> 
                        <div className='divider'/>
                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Estimated EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3'>value</h1>
                        <div className='divider'/> 

                        <div className='px-3 py-2 text-black bg-[#C2F23B] h-[40px] my-7 mx-3 rounded-lg font-medium'>
                            <h1>Reported EPS: </h1>
                        </div>
                        <h1 className='text-[#b5f2ed] my-7 py-2 mr-3 px-3'>—</h1>
                        <div className='divider'/>

                        <h1 className='text-[#b5f2ed] text-lg my-6 py-2 ml-9 mr-3'>—</h1>
                    </div>
                </div>
            </div>
            <img src={Stars} className='h-56 mr-9 mt-11'/>

            </div>

            <div className='fx'>
                <div className="tvw">
                    <TVtape/>
                </div>

                <div className='tech'>
                    <div className="tvtech">
                        <TechnicalAnalysis symbol='AMZN' className="gg" colorTheme="dark" width="100%"></TechnicalAnalysis>
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