#! C:\Users\nilus\OneDrive\Desktop\python pro\myenv\Scripts\python.exe

import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.info)
