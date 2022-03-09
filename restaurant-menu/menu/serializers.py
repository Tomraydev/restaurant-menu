from rest_framework import serializers
from .models import Menu, Dish


class DishSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="menu:dishes-detail")
    class Meta:
        model = Dish
        fields = '__all__'
        # extra_kwargs = {
        #     'url': {'view_name': 'menu/dishes', 'lookup_field': 'id'},
        # }


class MenuSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="menu:menus-detail")
    class Meta:
        model = Menu
        fields = '__all__'
        depth = 1
        # extra_kwargs = {
        #     'url': {'view_name': 'menu/menus', 'lookup_field': 'id'},
        #     'dishes': {'lookup_field': 'id'}
        # }
