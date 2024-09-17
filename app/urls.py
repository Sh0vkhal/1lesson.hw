from  django.urls import path
from .views import CarAPIView,CarDetailAPIView

urlpatterns = [
    path('api/v1/', CarAPIView.as_view()),
    path('api/v1/<int:pk>/', CarDetailAPIView.as_view()), 
]