# INF601 - Advanced Programming in Python
# Raymond Lee
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path


def getClosingPrice(ticker):
    # Function gets closing prices of last 10 trading days of a stock

    stockTicker = yf.Ticker(ticker)
    # Get historical market data of last 10 trading days
    historicalData = stockTicker.history("10d")

    # Create empty closing price list
    closingPrice_list = []

    # Loop to obtain closing price of each stock ticker
    for price in historicalData["Close"]:
        # Round price to 2 decimal places, add to closingPrice_list
        closingPrice_list.append(round(price, 2))

    return closingPrice_list


def printGraph(stock):
    # Function prints graph of stock closing prices of a stock

    # Create numpy array of a stock
    stockClosing_prices = np.array(getClosingPrice(stock))

    # Create appropriate x-axis values for graph
    days = list(range(1, len(stockClosing_prices)+1))

    # Plots the graph
    plt.plot(days, stockClosing_prices)

    # Produce y-axis max and min
    prices = getClosingPrice(stock)
    prices.sort()
    lowPrice = prices[0]
    highPrice = prices[-1]

    # Set x-axis and y-axis min and max
    plt.axis((1, 10, lowPrice-2, highPrice+2))

    # Set graph labels
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # Saving the graphs
    savefile = "charts/" + stock.upper() + ".png"
    plt.savefig(savefile)

    # Show graph
    plt.show()


# Begin program

stockTickers = ["MSFT", "AAPL", "SONY", "META", "AMZN"]
# Create charts directory to store png files of plot graphs
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

for stock in stockTickers:
    getClosingPrice(stock)
    printGraph(stock)

