from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from backend.serializers import UserSerializer
# Create your views here.

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class LoginView(KnoxLoginView):
  permission_classes = (permissions.AllowAny,)

  def post(self, request, format=None):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    return super(LoginView, self).post(request, format=None)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  authentication_classes = [TokenAuthentication]