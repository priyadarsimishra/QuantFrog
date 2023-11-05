import React from "react";
import Home from "./Components/Home";
import Stock from "./Components/Stock";
import { Route, Routes } from 'react-router-dom';


const App = () => {
    return (
        <div>
            <Routes>
                <Route path="/stock/:ticker" element={<Stock />} />
                <Route path="/" element={<Home />} />
            </Routes>
        </div>
    )
}
export default App;