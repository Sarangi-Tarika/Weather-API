from rest_framework import serializers
from .models import Weather, Stats

class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields =[ "date" ,"max_temp" ,"min_temp" ,"precipitation" , "station_name" ]



class StatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields =[ "date" ,"total_acc_ppt" ,"avg_min_temp" ,"avg_max_temp" , "station_name" ]