from django.urls import path
from .views import *

urlpatterns = [
    path('', EquationRootsCreateView.as_view(), name='roots'),
    path('solution/<int:pk>', EquationRootsDetailView.as_view(), name='solution'),
]