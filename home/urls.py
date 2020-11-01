from django.urls import path, include
from .views import (
    index,
    songView,
    handler404,
)

urlpatterns = [
    path('404/', handler404, name='404'),
    path('', index, name='veekay-index'),
    path('works/<str:typ>/<int:pk>/', songView, name='song-view'),
]