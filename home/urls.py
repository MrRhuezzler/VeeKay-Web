from django.urls import path, include
from .views import (
    index,
    songView,
)

urlpatterns = [
    path('', index, name='veekay-index'),
    path('works/<str:typ>/<int:pk>/', songView, name='song-view'),
]