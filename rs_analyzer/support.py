from logger import logger
from .difference import calculate
from rs_analyzer.models import Support as SM


class Support:

    def __init__(self):
        self.response = []

    def analyze_many(self, tickers, get_stock_data, market='Global'):
        for idx, ticker in enumerate(tickers):

            if SM.objects.filter(ticker=ticker, market=market).count() > 0:
                print(f'SKIP, {ticker} data already existing in {market} market')
                continue
            self.analyze(ticker, get_stock_data, market)

    def analyze(self, ticker, get_stock_data, market='Global'):
        ticker = ticker.upper()
        if SM.objects.filter(ticker=ticker, market=market).count() > 0:
            print(f'SKIP, {ticker} data already existing in {market} market')
            return []
        try:
            df = get_stock_data(ticker)
            current_price = round(df['close'][df.index[-1]], 2)
            support = {}
            support_list = []
            dates = {}
            counter = 0
            Range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            daterange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            s1 = None
            s2 = None

            for i in df.index:
                currentMin = min(Range, default=0)
                value = round(df["low"][i], 2)
                Range = Range[1:9]
                Range.append(value)
                daterange = daterange[1:9]
                daterange.append(i)

                if currentMin == min(Range, default=0):
                    counter += 1
                else:
                    counter = 0
                if counter == 5:
                    lastPivot = currentMin
                    dateloc = Range.index(lastPivot)
                    lastDate = daterange[dateloc]
                    if lastPivot != 0 and dates != 0:
                        support_list.append(lastPivot)
                        dates[lastPivot] = str(lastDate)
            support_list = list(dict.fromkeys(support_list))
            support_list.sort(reverse=True)
            print(support_list)
            for idx in range(len(support_list)):
                prev_price = support_list[idx]
                logger.debug(f'{current_price} > {prev_price} : {current_price > prev_price}')
                if current_price > prev_price:
                    s1 = support_list[idx]
                    s2 = support_list[idx + 1]
                    break

            support['current_price'] = current_price
            support['current_date'] = f'{df.index[-1]}'.split(' ')[0]
            if s1 > current_price:
                support['s1'] = "No support"
                support['s2'] = "No support"
            else:
                ps1 = round(calculate(current_price, s1), 2)
                ps2 = round(calculate(current_price, s2), 2)
                support['s1_date'] = dates[s1].split(' ')[0]
                support['s1_price'] = s1
                support['s1_diff'] = ps1
                support['s2_date'] = dates[s2].split(' ')[0]
                support['s2_price'] = s2
                support['s2_diff'] = ps2
                support['ticker'] = ticker
                support['market'] = market
                support_entry = SM(
                    ticker=support['ticker'],
                    current_price=support['current_price'],
                    current_date=support['current_date'],
                    s1_date=support['s1_date'],
                    s1_price=support['s1_price'],
                    s1_diff=support['s1_diff'],
                    s2_date=support['s2_date'],
                    s2_price=support['s2_price'],
                    s2_diff=support['s2_diff'],
                    market=support['market'],
                )
                support_entry.save()
                support['id'] = support_entry.id
            return [support]
        except Exception as e:
            logger.exception(e)
            return [str(e)]

