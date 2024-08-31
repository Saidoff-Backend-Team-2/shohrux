from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response


from account.models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginRequestSerializer

class UserRegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer



class UserLoginView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginRequestSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            user = CustomUser.objects.get(username=data['username'])
            logged_user = authenticate(username=user.username, password=data['password'])
            if logged_user:
                return Response(data=user.get_token())
            return Response(data={"User not found"})
        except CustomUser.DoesNotExist:
            return Response(data={"User not found"}, status=status.HTTP_400_BAD_REQUEST)