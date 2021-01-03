from logger import logger
from .difference import PercentDifference


p = PercentDifference()


class Resistance:

    def analyze(self, ticker, df, current_price):
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
            value = round(df["High"][i], 2)

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

        resistance_summary['current'] = current_price
        resistance_summary['current_date'] = df.index[-1]
        if r1 < current_price:
            resistance_summary['R1'] = "No resistance"
            resistance_summary['R2'] = "No resistance"
        else:
            pr1 = round(p.calculate(r1, current_price), 2)
            pr2 = round(p.calculate(r2, current_price), 2)
            resistance_summary['R1'] = {'date': dates[r1], 'price': r1, 'diff %': f'{pr1}'}
            resistance_summary['R2'] = {'date': dates[r2], 'price': r2, 'diff %': f'{pr2}'}
        # resistance_summary['resistance'] = resistance_list

        return {ticker: resistance_summary}
