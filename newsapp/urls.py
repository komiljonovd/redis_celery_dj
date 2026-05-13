from django.urls import path
from .views import NewsAPiView


urlpatterns = [
    path('api/v1/news-list/',NewsAPiView.as_view(),name='news-list'),

]