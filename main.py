# INF601 - Advanced Programming in Python
# Raymond Lee
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path


# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to a array in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

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

