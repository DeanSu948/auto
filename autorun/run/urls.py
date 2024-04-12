from django.urls import path, include
from rest_framework.routers import DefaultRouter
from run import views

router = DefaultRouter()
router.register('FlashInfo',views.FlashInfoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]