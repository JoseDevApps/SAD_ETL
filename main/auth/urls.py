from django.urls import path, include
from .views import UserViewSet, SuperUserViewSet, LoginViewSet
from rest_framework import routers
# from django.views.decorators.csrf import csrf_exempt

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'super', SuperUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]