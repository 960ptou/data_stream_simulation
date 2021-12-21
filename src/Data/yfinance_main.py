import sys
sys.path.insert(0, "Fetch")
sys.path.insert(0,"PreProcess")

from yfinance_fetch import *
from yfinance_preprocess import *
from fetch_util import *


def main():
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

            fetched_data = jsonData(stock_symbol, start_date = start_time, end_date = current_time)
            print(fetched_data)
            preprocessed_data = processData(fetched_data)
            print(preprocessed_data)

        else:
            print(f"{stock_symbol} is unavailble ")

        stop(test_time)






if __name__ == "__main__":
    main()