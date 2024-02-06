#! C:\Users\nilus\OneDrive\Desktop\python pro\myenv\Scripts\python.exe

import datetime
import time
from plyer import notification
import yfinance as yf

msft=yf.Ticker("MSFT")
data=msft.info

while True:
    notification.notify(
        title="MSFT data {}".format(datetime.date.today()),
        message="Current price={cp}\n DayLow={dl}\n DayHigh={dh}".format(
        cp=data["currentPrice"],
        dl=data["regularMarketDayLow"],
        dh=data["regularMarketDayHigh"],
        ),
         app_icon="C:/Users/nilus/Downloads/flying-money.ico",
         timeout=10
    )
    time.sleep(2*60*60)
 