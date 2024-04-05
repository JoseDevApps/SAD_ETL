from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from .serializers import UserSerializer, SuperUserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class SuperUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer
    permission_classes = (IsAuthenticated,)

class LoginViewSet(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed("User or password didn't match")
        if not user.check_password(password):
            raise AuthenticationFailed("User or password didn't match")
        token = Token.objects.get_or_create(user=user)
        response  = Response()
        response.set_cookie(key='token', value=token[0], httponly=True)
        response.data = {
            'token': str(token[0])
        }
        # Ejmplo de cabecera 
        # Authorization: Token 488c9b423c4f886de4807c40d8c53e4b9c4c1d7d
         
        return response
