from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "api"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"dishes", views.DishViewSet, basename="dishes")
router.register(r"menus", views.MenuViewSet, basename="menus")

urlpatterns = [
    path("", include(router.urls)),
]
