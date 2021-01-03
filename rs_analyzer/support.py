from logger import logger
from .difference import PercentDifference


p = PercentDifference()


class Support:

    def analyze(self, ticker, df, current_price):
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
            value = round(df["Low"][i], 2)
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
        support_list.sort(reverse=True)
        for idx in range(len(support_list)):
            prev_price = support_list[idx]
            logger.debug(f'{current_price} > {prev_price} : {current_price > prev_price}')
            if current_price > prev_price:
                s1 = support_list[idx]
                s2 = support_list[idx + 1]
                break

        support['current_price'] = current_price
        support['current_date'] = df.index[-1]
        if s1 > current_price:
            support['S1'] = "No support"
            support['S2'] = "No support"
        else:
            ps1 = round(p.calculate(current_price, s1), 2)
            ps2 = round(p.calculate(current_price, s2), 2)
            support['S1'] = {'date': dates[s1], 'price': s1, 'diff %': f'{ps1}'}
            support['S2'] = {'date': dates[s2], 'price': s2, 'diff %': f'{ps2}'}

        # support['support'] = support_list

        return {ticker: support}
