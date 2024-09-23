from rest_framework import serializers
import re

class WeatherRequestSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=100, required=True)        
    page = serializers.IntegerField(default=1)
    per_page = serializers.IntegerField(default=10)
    show_all = serializers.BooleanField(default=False)

    def  validate_q(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Destination param must be less than 100 characters")
        return value
    def validate_page(self, value):
        if value < 1:
            raise serializers.ValidationError("Page param must be greater than 0")
        return value
    def validate_per_page(self, value):
        if value < 1:
            raise serializers.ValidationError("Per_page param must be greater than 0")
        return value
    def validate_show_all(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Show_all param must be a boolean")
        return value
        
    
            
    
    
