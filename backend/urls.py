from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views
from backend.views import index_view, LoginView, UserViewSet, NicknameViewSet, QuoteViewSet, LeaderbordPositionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,)
router.register(r'nicknames', NicknameViewSet)
router.register(r'quotes', QuoteViewSet)
router.register(r'mongolen_board', LeaderbordPositionViewSet)

urlpatterns = [
  path(r'auth/login/', LoginView.as_view(), name='knox_login'),
  path(r'auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
  path(r'auth/logoutall/',  knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
  path(r'', include(router.urls)),
  path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]