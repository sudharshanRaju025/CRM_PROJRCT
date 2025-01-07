from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import user
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
# from rest_framework.permissions import IsAuthenticated  
# from rest_framework.authentication import TokenAuthentication

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(generics.GenericAPIView):

    queryset=user.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user is not None:
            return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
 