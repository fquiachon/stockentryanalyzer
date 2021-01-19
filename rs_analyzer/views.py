from .resistance import Resistance
from .support import Support
from logger import logger
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .gateway.yfinance_api import get_stock_data, NOW
from .gateway.pse_api import get_data
from .models import Support as SM
from .serializers import SupportSerializer


class PSESupportView(APIView):
    def get(self, request):
        ser = SupportSerializer(SM.objects.filter(market='PSE'), many=True)
        response = Response(ser.data, 200)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def post(self, request, ticker):
        received_json_data = json.loads(request.body.decode("utf-8"))
        tickers = received_json_data['tickers'].split(',')
        analyzer = Support()
        analyzer.analyze_many(tickers, get_data, 'PSE')
        response = Response({'status': 'Accepted'}, 201)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def handle_exception(self, exc):
        return Response({'Error': str(exc)}, 400)


class PSEResistanceView(APIView):
    def handle_exception(self, exc):
        return Response({'Error': str(exc)})

    def get(self, request):
        support_list = SM.objects.all()
        if support_list:
            ser = SupportSerializer(SM.objects.all())
            response = Response(ser.data, 200)
        else:
            response = Response([], 200)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        tickers = received_json_data['tickers'].split(',')
        analyzer = Resistance()
        data = analyzer.analyze_many(tickers, get_data, 'PSE')
        response = Response(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class SupportView(APIView):
    def get(self, request):
        support_list = SM.objects.filter(market='Global')
        if support_list:
            ser = SupportSerializer(support_list, many=True)
            response = Response(ser.data, 200)
        else:
            response = Response([], 200)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def post(self, request, ticker):
        # received_json_data = json.loads(request.body.decode("utf-8"))
        # tickers = received_json_data['tickers'].split(',')
        analyzer = Support()
        analyzer.analyze(ticker, get_stock_data)
        response = Response({'status': 'Accepted'}, 201)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def handle_exception(self, exc):
        return Response({'Error': str(exc)}, 400)


class ResistanceView(APIView):
    def handle_exception(self, exc):
        return Response({'Error': str(exc)})

    def get(self, request):
        ticker = "x"
        analyzer = Resistance()
        try:
            data, code = analyzer.analyze(ticker, get_stock_data), 200
        except Exception as e:
            logger.error(str(e))
            data, code = {'Error': str(e)}, 400
        response = Response(data, code)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        tickers = received_json_data['tickers'].split(',')
        analyzer = Resistance()
        data = analyzer.analyze_many(tickers, get_stock_data)
        response = Response(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class IndexView(APIView):
    def get(self, request):
        return Response("Welcome to Stock Entry Analyzer API")

    def handle_exception(self, exc):
        return Response({'Error': str(exc)}, 400)
