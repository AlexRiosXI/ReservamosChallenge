from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from weather.serializers import WeatherRequestSerializer

from weather.fetch.api_forecast import fetch_forecast

# Create your views here.
class WeatherAPIHealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    

class WeatherAPIView(APIView):
    def get(self, request):
        serializer = WeatherRequestSerializer(data=request.GET)
        
        if not serializer.is_valid():
            if "q" in serializer.errors:
                return Response({"status": "destination error", "message": serializer.errors["q"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "page" in serializer.errors:
                return Response({"status": "page error", "message": serializer.errors["page"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "per_page" in serializer.errors:
                return Response({"status": "per_page error", "message": serializer.errors["per_page"][0]}, status=status.HTTP_400_BAD_REQUEST)
            if "show_all" in serializer.errors:
                return Response({"status": "show_all error", "message": serializer.errors["show_all"][0]}, status=status.HTTP_400_BAD_REQUEST)
        destinaions = fetch_forecast(serializer.data["q"], serializer.data["page"], serializer.data["per_page"], serializer.data["show_all"])
        if destinaions.status_code == 404:
            return Response({"status": "not found", "message": "Destination not found"}, status=status.HTTP_404_NOT_FOUND)
        if destinaions.status_code != 201:            
            return Response({"status": "error", "message": "Error fetching destinations"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"status": "ok", "data": destinaions.json()}, status=status.HTTP_200_OK)