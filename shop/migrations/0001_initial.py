# Generated by Django 3.0.5 on 2020-09-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('CML', 'COFFEE_MACHINE_LARGE'), ('CMS', 'COFFEE_MACHINE_SMALL'), ('EM', 'ESPRESSO_MACHINE')], max_length=100)),
                ('water_line', models.BooleanField(default=False)),
                ('SKU', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CoffePod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('CPL', 'COFFEE_POD_LARGE'), ('CPM', 'COFFEE_POD_SMALL'), ('EP', 'ESPRESSO_POD')], max_length=100)),
                ('coffee_flavor', models.CharField(choices=[('CFV', 'COFFEE_FLAVOR_VANILLA'), ('CFC', 'COFFEE_FLAVOR_CARAMEL'), ('CFP', 'COFFEE_FLAVOR_PSL'), ('CFM', 'COFFEE_FLAVOR_MOCHA'), ('CFH', 'COFFEE_FLAVOR_HAZELNUT')], max_length=100)),
                ('pack_size', models.CharField(choices=[('1dozen', '1 dozen (12)'), ('3dozen', '3 dozen (36)'), ('5dozen', '5 dozen (60)'), ('7dozen', '7 dozen (84)')], max_length=100)),
                ('SKU', models.CharField(max_length=150)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
    ]