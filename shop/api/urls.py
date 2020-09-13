
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter 
router= DefaultRouter()
router.register('large-machines',views.LargeMachinesViewSet,basename='large-machines')
router.register('large-pods',views.LargePodsViewSet,basename='large-pods')
router.register('vanilla-pods',views.VanillaPodsViewSet,basename='vanilla-pods')
router.register('espresso-machines',views.EspressoMachinesViewSet,basename='espresso-machines')
router.register('small-pods',views.SmallPodsViewSet,basename='small-pods')
router.register('7dozen-pods',views.PodsSevenDozenViewSet,basename='7dozens-pods')
router.register('water-line-machines',views.WaterLineMachinesViewSet,basename='water-line-machines')


app_name='shop'

urlpatterns = [  
    path('',include(router.urls)),     
]
