from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


# создание датчика и получение списка с краткой информацией
class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# изменение датчика и получение данных по конкретному датчику
class SensorRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# добавляет измерение
class MeasurementAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer














# изменение и получение инфы о датчике конкретном??
# class SensorAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer


