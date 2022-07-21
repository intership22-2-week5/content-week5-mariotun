from django.db import router

#Django rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import TecladoViewSet,RatonViewSet,MonitorViewSet,ComputadoraViewSet,OrdenViewSet,PlacaBaseViewSet,AltavozViewSet,ProcesadorViewSet,DispositivoSalidaViewSet,DispositivoEntradaViewSet

router = DefaultRouter()
#router.register(r'dispoentrada',DispositivoEntradaViewSet)

router.register(r'placabase',PlacaBaseViewSet)
router.register(r'altavoz',AltavozViewSet)
router.register(r'procesador',ProcesadorViewSet)
router.register(r'dispsalida',DispositivoSalidaViewSet)
router.register(r'dispentrada',DispositivoEntradaViewSet)

router.register(r'teclado',TecladoViewSet)
router.register(r'raton',RatonViewSet)
router.register(r'monitor',MonitorViewSet)
router.register(r'computadora',ComputadoraViewSet)
router.register(r'orden',OrdenViewSet)



urlpatterns = router.urls

urlpatterns += [

]
