from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import BookViewSet
 
from api_app import views
 
router = routers.DefaultRouter()
router.register(r'book', BookViewSet),
 
urlpatterns = [
    path('', include(router.urls)),
]