from django.urls import include, path
from .views import *

urlpatterns = [
    path('', EquationRootsCreateView.as_view(), name='roots'),
    path('solution/<int:pk>', EquationRootsDetailView.as_view(), name='solution'),
    #path('', index, name='home'),
]