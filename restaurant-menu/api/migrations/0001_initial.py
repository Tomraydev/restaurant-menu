# fmt: off

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preparation_time', models.DurationField()),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='date modified')),
                ('is_vegan', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='date modified')),
                ('dishes', models.ManyToManyField(blank=True, to='api.dish')),
            ],
            options={
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
