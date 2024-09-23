from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from weather.serializers import WeatherRequestSerializer
from weather.fetch.api_forecast import fetch_forecast

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class WeatherAPIHealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    

class WeatherAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, description="Destination query", type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER, required=False, default=1),
            openapi.Parameter('per_page', openapi.IN_QUERY, description="Number of results per page", type=openapi.TYPE_INTEGER, required=False, default=10),
            openapi.Parameter('show_all', openapi.IN_QUERY, description="Show all results", type=openapi.TYPE_BOOLEAN, required=False, default=False)
        ],
        responses={200: 'Success'}
    )
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
        try:
            destinaions = fetch_forecast(serializer.data["q"], serializer.data["page"], serializer.data["per_page"], serializer.data["show_all"])
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if len(destinaions) == 0:
            return Response({"status": "not found", "message": "Destination not found"}, status=status.HTTP_404_NOT_FOUND)
    
        
        return Response({"status": "ok", "data": destinaions}, status=status.HTTP_200_OK)