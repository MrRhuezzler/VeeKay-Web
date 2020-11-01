from django.urls import path, include
from .views import (
    index,
    songView,
    _404,
)

handler404 = 'home.views._404'

urlpatterns = [
    path('', index, name='veekay-index'),
    path('works/<str:typ>/<int:pk>/', songView, name='song-view'),
    path('404/', _404, name='404'),
]