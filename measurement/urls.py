from django.urls import path
from measurement.views import *

urlpatterns = [
    path('sensors/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('sensors/detail/<int:pk>/', SensorAPIRetrieve.as_view()),
    path('measurements/', MeasurementsAPIList.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
