from django.http import HttpResponse
from .resistance import Resistance
from .support import Support
from django.http import JsonResponse
from logger import logger
from rest_framework.decorators import api_view
import json
from rest_framework.views import APIView
from rest_framework.response import Response


class SupportView(APIView):
    def get(self, request, ticker):
        ticker = ticker.upper()
        analyzer = Support()
        try:
            data = analyzer.analyze(ticker)
        except Exception as e:
            data = {'Error': str(e)}
        return Response(data)

    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        tickers = received_json_data['tickers'].split(',')
        analyzer = Support()
        data = analyzer.analyze_many(tickers)
        return Response(data)

    def handle_exception(self, exc):
        return Response({'Error': str(exc)})


class ResistanceView(APIView):
    def handle_exception(self, exc):
        return Response({'Error': str(exc)})

    def get(self, request, ticker):
        ticker = ticker.upper()
        analyzer = Resistance()
        try:
            data = analyzer.analyze(ticker)
        except Exception as e:
            logger.error(str(e))
            data = {'Error': str(e)}
        return Response(data)

    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        tickers = received_json_data['tickers'].split(',')
        analyzer = Resistance()
        data = analyzer.analyze_many(tickers)
        return Response(data)


class IndexView(APIView):
    def get(self, request):
        return Response("Hello, world. You're at the polls index.")

    def handle_exception(self, exc):
        return Response({'Error': str(exc)})
