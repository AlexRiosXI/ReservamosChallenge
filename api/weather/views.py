from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class WeatherAPIHealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    

class WeatherAPIView(APIView):
    def get(self, request):
        print("get")
        return Response({"status": "ok"}, status=status.HTTP_200_OK)