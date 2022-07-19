from django.db import router

#Django rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import TipoViewSet,MultimediaViewSet,ObrasArteViewSet,AuthorViewSet,Author_ObrasArteViewSet,PortafolioViewSet,ExposicionViewSet,UserViewSet

router = DefaultRouter()
router.register(r'tipo',TipoViewSet)
router.register(r'multimedia',MultimediaViewSet)
router.register(r'obrasarte',ObrasArteViewSet)
router.register(r'autor',AuthorViewSet)
router.register(r'autorobra',Author_ObrasArteViewSet)
router.register(r'portafolio',PortafolioViewSet)
router.register(r'exposicion',ExposicionViewSet)
router.register(r'user',UserViewSet)

urlpatterns = router.urls

urlpatterns += [

]