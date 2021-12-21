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
    names = []
    itemsDetails = ["Date", "Open", "High", "Low", "Close", "Volume", "Dividends", "StockSplits"]


    for items in tickerData.values:
        name = f"{stockSymbol}-{str(items[0])}"
        data = fetch.data(name,
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
        names.append(name)

    details = fetch.details(names, itemsDetails)
    dataBatch = fetch.dataBatch(details, dataList)

    return dataBatch

def main():
    # Stop by exiting
    test_time = FIFTEEN_MINUTES
    stock_symbol = "AAPL"
    
    while True:
        current_time = now()
        start_time = create_time_from_today(hour = START_HOUR, minute = START_MINUTE)
        end_time = create_time_from_today(hour = END_HOUR, minute = END_MINUTE)

        print(f"It's currently {current_time.hour}:{current_time.minute}:({time_format(current_time)})")
        
        if between_time(current_time, start_time, end_time):

            start_time = minutes_before_now(test_time)
            current_time = current_time
            names = [stock_symbol]
            print(f"From:{start_time} -- To:{current_time}")
            print(json.loads(jsonData(stock_symbol, start_date = start_time, end_date = current_time)))

        else:
            print(f"{stock_symbol} is unavailble ")
            
        stop(test_time)


if __name__ == "__main__":
    main()
    
    
    

    
