from rest_framework import routers
from games.api import views

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'haves', views.HaveViewSet)
router.register(r'passes', views.PassViewSet)
router.register(r'shows', views.ShowViewSet)

urlpatterns = router.urls
