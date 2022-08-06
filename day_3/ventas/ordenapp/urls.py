from unicodedata import name
from django.db import router
from django.urls import path

#Django rest framework
from rest_framework.routers import DefaultRouter

#views
#from .views import ComponenteTipoView,TecladoViewSet,RatonViewSet,MonitorViewSet,ComputadoraViewSet,OrdenViewSet,DetalleOrdenViewSet, PlacaBaseViewSet,AltavozViewSet,ProcesadorViewSet,DispositivoSalidaViewSet,DispositivoEntradaViewSet
from .viewsets.component import PlacaBaseViewSet,AltavozViewSet,ProcesadorViewSet,TecladoViewSet,RatonViewSet,MonitorViewSet
from .viewsets.computer import ComputadoraViewSet
from .viewsets.order import OrdenViewSet,DetalleOrdenViewSet,ComponenteTipoView


router = DefaultRouter()
#router.register(r'dispoentrada',DispositivoEntradaViewSet)

router.register(r'placabase',PlacaBaseViewSet)
router.register(r'altavoz',AltavozViewSet)
router.register(r'procesador',ProcesadorViewSet)
#router.register(r'dispsalida',DispositivoSalidaViewSet)
#router.register(r'dispentrada',DispositivoEntradaViewSet)

router.register(r'teclado',TecladoViewSet)
router.register(r'raton',RatonViewSet)
router.register(r'monitor',MonitorViewSet)
router.register(r'computadora',ComputadoraViewSet)
router.register(r'orden',OrdenViewSet)
router.register(r'detalleorden',DetalleOrdenViewSet)

#filtros
#router.register(r'componentetipo',ComponenteTipoView)



urlpatterns = router.urls

urlpatterns += [
    path('componentetipo/',ComponenteTipoView.as_view(),name='ComponenteOperations')
]
