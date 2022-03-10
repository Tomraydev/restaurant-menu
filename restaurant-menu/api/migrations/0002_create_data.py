# fmt: off
from datetime import timedelta

from api.models import Dish, Menu
from django.db import migrations


def create_initial_data(apps, schema_editor):
    # Menus
    empty_menu = Menu(name='Puste menu', description='Nie powinno być widoczne dla niezalogowanych użytkowników.')
    empty_menu.save()
    breakfast = Menu(name='Śniadaniowe', description='Dostępne do godziny 11.')
    breakfast.save()
    lunch = Menu(name='Obiadowe', description='Dostępne do godziny 18.')
    lunch.save()
    dinner = Menu(name='Kolacyjne', description='Dostępne po godzinie 18.')
    dinner.save()

    # Dishes
    ## breakfast
    breakfast.dishes.create(
        name = 'Jajecznica',
        description = 'Jajecznica z 3 jaj na boczku.',
        price = 10.00,
        preparation_time = timedelta(minutes=10),
        # date_added = '2022-02-01',
        # date_modified = '2022-02-10',
        is_vegan = False,
    )
    breakfast.dishes.create(
        name = 'Jajecznica Wege',
        description = 'Jajecznica z 3 jaj na maśle.',
        price = 9.00,
        preparation_time = timedelta(minutes=10),
        # date_added = '2022-02-02',
        # date_modified = '2022-02-11',
        is_vegan = True,
    )
    breakfast.dishes.create(
        name = 'Naleśniki z dżemem',
        description = 'Naleśniki z dżemem (4 szt.) Różne owoce.',
        price = 12.00,
        preparation_time = timedelta(minutes=12),
        is_vegan = True,
    )
    breakfast.dishes.create(
        name = 'Omlet z wędzonym łososiem',
        description = 'Omlet z wędzonym łososiem, suszonymi pomidorami, kaparami i cebulką.',
        price = 21.00,
        preparation_time = timedelta(minutes=15),
        is_vegan = False,
    )

    ## lunch
    lunch.dishes.create(
        name = 'Łosoś z grilla',
        description = '+ ziemniak w folii, bukiet sałat.',
        price = 41.00,
        preparation_time = timedelta(minutes=20),
        is_vegan = False,
    )
    lunch.dishes.create(
        name = 'Gulasz wołowo-wieprzowy',
        description = 'kasza gryczana, ogórek konserwowy',
        price = 30.00,
        preparation_time = timedelta(minutes=10),
        is_vegan = False,
    )
    lunch.dishes.create(
        name = 'Rostbef z sosem pieprzowym',
        description = '+ ziemniaki grillowane, bukiet sałat',
        price = 55.00,
        preparation_time = timedelta(minutes=20),
        is_vegan = False,
    )

    ## dinner
    dinner.dishes.create(
        name = 'Guinness 0.5L',
        description = 'Piwo ciemne, lane.',
        price = 17.00,
        preparation_time = timedelta(minutes=1),
        is_vegan = True,
    )
    dinner.dishes.create(
        name = 'Miody Ałtaju 0.5L',
        description = 'Polskie Browary Sezonowe Miody Ałtaju Piwo jasne 500 ml',
        price = 12.00,
        preparation_time = timedelta(minutes=1),
        is_vegan = True,
    )

    ## common
    common_dishes = [
        Dish(
            name = 'Herbata w Dzbanku',
            description = 'Czarna, zielona, miętowa, owocowa, earl grey',
            price = 8.00,
            preparation_time = timedelta(minutes=5),
            is_vegan = True
        ),
        Dish(
            name = 'Kawa (Vergnano)',
            description = 'Kawa parzona. Opcjonalnie mleko i cukier.',
            price = 8.00,
            preparation_time = timedelta(minutes=5),
            is_vegan = True
        ),
        Dish(
            name = 'Coca-Cola 0.2L',
            description = 'Zimna, z lodówki.',
            price = 6.00,
            preparation_time = timedelta(minutes=1),
            # date_added = '2022-03-01',
            # date_modified = '2022-03-05',
            is_vegan = True
        ),
    ]
    for dish in common_dishes:
        dish.save()
        breakfast.dishes.add(dish)
        lunch.dishes.add(dish)
        dinner.dishes.add(dish)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]
    operations = [migrations.RunPython(create_initial_data)]
