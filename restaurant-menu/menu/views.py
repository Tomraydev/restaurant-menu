from django.db.models import Count
from rest_framework import viewsets, permissions, generics
from .serializers import MenuSerializer, DishSerializer
from .models import Menu, Dish


class DishViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    model = Dish

class MenuViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    model = Menu

    def get_queryset(self):
        queryset = Menu.objects.all()
        sort = self.request.query_params.get('sort')
        name = self.request.query_params.get('name')
        added_after = self.request.query_params.get('added_after')
        added_before = self.request.query_params.get('added_before')
        updated_after = self.request.query_params.get('updated_after')
        updated_before = self.request.query_params.get('updated_before')


        # filtering
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
        if sort=='name':
            queryset = queryset.order_by('name')
        elif sort=='num_dishes':
            queryset = queryset.select_related() \
                .annotate(num_Dish=Count('dishes__id')) \
                .order_by('num_Dish')

        return queryset
