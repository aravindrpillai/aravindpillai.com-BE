from util.http_util import HttpUtil
from rest_framework.views import APIView

class StocksAPI(APIView):
    
    def get(self, request, ticker):
        if not ticker:
            return HttpUtil.respond(400, "Invalid Ticker", None)
        
        
        return HttpUtil.respond(200, None, {"ticker" : ticker})
