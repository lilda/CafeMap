from rest_framework import routers
from django.urls import include, path

# from django.conf.urls import url, include
from . import views
# from .views import CafeViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('cafes', views.CafeViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('cafelikes', views.Cafe_LikeViewSet)
router.register('cafeunlikes', views.Cafe_UnlikeViewSet)
router.register('reviewlikes', views.Review_LikeViewSet)
router.register('reviewunlikes', views.Review_UnlikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]