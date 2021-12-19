import yfinance as yf
import fetch
import simplejson as json
from fetch_util import *

FIFTEEN_MINUTES = 15
FIVE_MINUTES = 5

START_HOUR = 9
START_MINUTE = 30
END_HOUR = 16
END_MINUTE = 0


def getData(stockSymbol, intervals ='1d', start_date = '2000-1-1',
        end_date = time_format(now()) ):
    
    tickerData = yf.Ticker(stockSymbol)
    tickerDf = tickerData.history(interval = intervals, start = start_date, end = end_date)
    tickerDf.reset_index(inplace = True)
    return tickerDf

def jsonData(stockSymbol,
        intervals ='1m',
        start_date = time_format(minutes_before_now(FIFTEEN_MINUTES)),
        end_date = time_format(now()) ):

    tickerData = getData(stockSymbol, intervals, start_date, end_date)

    dataList = []
    names = stockSymbol
    itemsDetails = list(tickerData.columns)


    for items in tickerData.values:
        data = fetch.data(stockSymbol,
                          Date          = str(items[0]),
                          Open          = items[1],
                          High          = items[2],
                          Low           = items[3],
                          Close         = items[4],
                          Volume        = items[5],
                          Dividends     = items[6],
                          StockSplits   = items[7]
                    )
        dataList.append(data)

    details = fetch.details(names, itemsDetails)
    dataBatch = fetch.dataBatch(details, dataList)

    return dataBatch

def main():
    # Stop by exiting
    test_time = 4
    while True:
        current_time = now()
        start_time = create_time_from_today(hour = START_HOUR, minute = START_MINUTE)
        end_time = create_time_from_today(hour = END_HOUR, minute = END_MINUTE)
        stock_symbol = "AAPL"
        
        if not(between_time(current_time, start_time, end_time)):
            print(f"{stock_symbol} is unavailble because")
            print(f"It's currently {current_time.hour}:{current_time.minute}:({time_format(current_time)})")
        else:
            print(jsonData(stock_symbol, start_date = time_format(minutes_before_now(test_time))))

        print(f"Sleeping for {test_time} minutes")
        stop(test_time)


if __name__ == "__main__":
    main()
    
    
    

    
