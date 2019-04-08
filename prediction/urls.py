from django.urls import path, include
from .views import *
urlpatterns = [
    path('predecir', LandingView.as_view(), name="predicciones"),
    path('descubrir', Evaluated.as_view(), name="evaluacion de datos"),
]
