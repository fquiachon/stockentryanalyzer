from django.http import HttpResponse
from .resistance import Resistance
from .support import Support
from .world.gateway import get_stock_data
from django.http import JsonResponse
from logger import logger


def support(request, ticker):
    ticker = ticker.upper()
    analyzer = Support()
    try:
        df, current_price = get_stock_data(ticker)
        data = analyzer.analyze(ticker, df, current_price)
    except Exception as e:
        data = {'Error': str(e)}
    return JsonResponse(data)


def resistance(request, ticker):
    ticker = ticker.upper()
    analyzer = Resistance()
    try:
        df, current_price = get_stock_data(ticker)
        data = analyzer.analyze(ticker, df, current_price)
    except Exception as e:
        logger.error(str(e))
        data = {'Error': str(e)}
    return JsonResponse(data)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
