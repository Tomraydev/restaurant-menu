from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .filters import MenuFilter
from .models import Dish, Menu
from .serializers import DishSerializer, MenuSerializer


class DishViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """CRUD operations for a collection of dishes or a single dish"""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    model = Dish

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = DishSerializer(item)
        return Response(serializer.data)


class MenuViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """CRUD operations for a collection of menus or a single menu"""

    filter_backends = (MenuFilter,)  # for swagger query parameters.
    serializer_class = MenuSerializer
    model = Menu

    def filter_queryset(self, queryset):
        """filter_queryset needs to be overridden, so swagger can display query parameters."""
        return queryset

    def get_queryset(self):
        queryset = Menu.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()

        sort = request.query_params.get("sort")
        name = request.query_params.get("name")
        added_after = request.query_params.get("added_after")
        added_before = request.query_params.get("added_before")
        updated_after = request.query_params.get("updated_after")
        updated_before = request.query_params.get("updated_before")

        # filtering
        if not request.user.is_authenticated:  # don't show empty menus to non-users
            queryset = queryset.select_related().annotate(num_Dish=Count("dishes__id")).filter(num_Dish__gte=1)
        if name:
            queryset = queryset.filter(name=name)
        if added_after:
            queryset = queryset.filter(date_added__gte=added_after)
        if added_before:
            queryset = queryset.filter(date_added__lt=added_before)
        if updated_after:
            queryset = queryset.filter(date_added__gte=updated_after)
        if updated_before:
            queryset = queryset.filter(date_added__lt=updated_before)

        # sorting
        if sort == "name":
            queryset = queryset.order_by("name")
        elif sort == "num_dishes":
            queryset = queryset.select_related().annotate(num_Dish=Count("dishes__id")).order_by("-num_Dish")

        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer.data)
