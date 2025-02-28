from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)  # Автоматическая маршрутизация для TaskViewSet

urlpatterns = [
    path("", include(router.urls)),  # Подключаем маршруты роутера
]
