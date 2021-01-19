from logger import logger
from .difference import calculate


class Resistance:

    def __init__(self):
        self.response = []

    def analyze_many(self, tickers, get_stock_data, market='Global'):
        for idx, ticker in enumerate(tickers):
            self.response.append(self.analyze(ticker, get_stock_data, market))
            self.response.append({'Status': f'{idx+1}/{len(tickers)} Completed'})
        return self.response

    def analyze(self, ticker, get_stock_data, market='Global'):
        ticker = ticker.upper()
        try:
            df = get_stock_data(ticker)
            current_price = round(df['close'][-1], 2)
            resistance_summary = {}
            resistance_list = []
            dates = {}
            counter = 0
            Range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            daterange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            r1 = None
            r2 = None

            for i in df.index:
                currentMax = max(Range, default=0)
                value = round(df["high"][i], 2)

                Range = Range[1:9]
                Range.append(value)
                daterange = daterange[1:9]
                daterange.append(i)

                if currentMax == max(Range, default=0):
                    counter += 1
                else:
                    counter = 0
                if counter == 5:
                    last_pivot = currentMax
                    dateloc = Range.index(last_pivot)
                    lastDate = daterange[dateloc]
                    resistance_list.append(last_pivot)
                    dates[last_pivot] = str(lastDate)

            resistance_list.sort(reverse=True)

            for idx in range(len(resistance_list)):
                prev_price = resistance_list[idx]
                logger.debug(f'{current_price} > {prev_price} : {not current_price < prev_price}')
                if not current_price < prev_price:
                    r1 = resistance_list[idx - 1]
                    r2 = resistance_list[idx - 2]
                    break

            resistance_summary['id'] = 26
            resistance_summary['current_price'] = current_price
            resistance_summary['current_date'] = f'{df.index[-1]}'.replace('T', ' ')
            if r1 < current_price:
                resistance_summary['r1'] = "No Resistance"
                resistance_summary['r2'] = "No Resistance"
            else:
                pr1 = round(calculate(r1, current_price), 2)
                pr2 = round(calculate(r2, current_price), 2)
                resistance_summary['r1_date'] = dates[r1]
                resistance_summary['r1_price'] = r1
                resistance_summary['r1_diff'] = pr1
                resistance_summary['r2_date'] = dates[r2]
                resistance_summary['r2_price'] = r2
                resistance_summary['r2_diff'] = pr2
                resistance_summary['ticker'] = ticker
            return [resistance_summary]
        except Exception as e:
            return [str(e)]
