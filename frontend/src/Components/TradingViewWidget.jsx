// TradingViewWidget.jsx

import React, { useEffect, useRef } from 'react';

let tvScriptLoadingPromise;

export default function TradingViewWidget() {
  const onLoadScriptRef = useRef();

  useEffect(
    () => {
      onLoadScriptRef.current = createWidget;

      if (!tvScriptLoadingPromise) {
        tvScriptLoadingPromise = new Promise((resolve) => {
          const script = document.createElement('script');
          script.id = 'tradingview-widget-loading-script';
          script.src = 'https://s3.tradingview.com/tv.js';
          script.type = 'text/javascript';
          script.onload = resolve;

          document.head.appendChild(script);
        });
      }

      tvScriptLoadingPromise.then(() => onLoadScriptRef.current && onLoadScriptRef.current());

      return () => onLoadScriptRef.current = null;

      function createWidget() {
        if (document.getElementById('tradingview_a8c26') && 'TradingView' in window) {
          new window.TradingView.widget({
            autosize: true,
            symbol: "AMZN",
            interval: "D",
            timezone: "Etc/UTC",
            theme: "dark",
            style: "2",
            locale: "en",
            enable_publishing: false,
            allow_symbol_change: true,
            container_id: "tradingview_a8c26"
          });
        }
      }
    },
    []
  );

  return (
    <div className='tradingview-widget-container' style={{ height: "100%", width: "100%" , padding: "25px" }}>
      <div id='tradingview_a8c26' style={{ height: "calc(100%)", width: "100%" }} />
      
    </div>
  );
}
