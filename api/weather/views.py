from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from weather.serializers import WeatherRequestSerializer

# Create your views here.
class WeatherAPIHealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    

class WeatherAPIView(APIView):
    def get(self, request):
        serializer = WeatherRequestSerializer(data=request.GET)
        
        if not serializer.is_valid():
            if "q" in serializer.errors:
                print(serializer.errors)
                return Response({"status": "destination error", "message": serializer.errors["q"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "page" in serializer.errors:
                return Response({"status": "page error", "message": serializer.errors["page"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "per_page" in serializer.errors:
                return Response({"status": "per_page error", "message": serializer.errors["per_page"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "show_all" in serializer.errors:
                return Response({"status": "show_all error", "message": serializer.errors["show_all"][0]}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)