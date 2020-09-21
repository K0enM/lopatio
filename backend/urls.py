from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views
from backend.views import index_view, LoginView, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,)

urlpatterns = [
  path(r'auth/login/', LoginView.as_view(), name='knox_login'),
  path(r'auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
  path(r'auth/logoutall/',  knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
  path(r'', include(router.urls)),
  path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]