from django.urls import path
from .views import *

urlpatterns = [
    path('', BallNumberCreateView.as_view(), name='entry'),
    path('guess/<int:pk>', BallNumberDetailView.as_view(), name='guess'),
]