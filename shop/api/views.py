from shop.models import CoffeeMachine,CoffePod
from .serializers import machineSerializer,podSerializer
from rest_framework import viewsets,mixins



# determine all large machines
class LargeMachinesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = machineSerializer
    def get_queryset(self):
        return CoffeeMachine.objects.filter(product_type='CML')

# determine all large pods
class LargePodsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = podSerializer
    def get_queryset(self):
        return CoffePod.objects.filter(product_type='CPL')

# determine all espresso vanilla pods 

class VanillaPodsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = podSerializer
    def get_queryset(self):
        return CoffePod.objects.filter(coffee_flavor='CFV')


# determine all espresso machines

class EspressoMachinesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = machineSerializer
    def get_queryset(self):
        return CoffeeMachine.objects.filter(product_type='EM')


# determine all small pods

class SmallPodsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = podSerializer
    def get_queryset(self):
        print(CoffePod.objects.first().product_type)
        return CoffePod.objects.filter(product_type='COFFEE_POD_SMALL')

# determine all pods 7 dozens
class PodsSevenDozenViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = podSerializer
    def get_queryset(self):
        return CoffePod.objects.filter(pack_size='7dozen')

# determine machines with water line

class WaterLineMachinesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = machineSerializer
    def get_queryset(self):
        return CoffeeMachine.objects.filter(water_line=True)