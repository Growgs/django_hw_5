# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer


# получение краткой информации по датчикам и создание датчика:
class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# изменение датчика:
class SensorAPIUpdate(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# получение данных по конкретному датчику
class SensorAPIRetrieve(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# внесение измерений
class MeasurementsAPIList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
