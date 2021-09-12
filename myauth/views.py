from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import status, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import SlidingToken

from myauth.models import User

from .serializers import AuthenticationResponseSerializer, AuthenticationSerializer


class AuthenticationViewSet(GenericViewSet):
    serializer_class = AuthenticationSerializer

    @action(detail=False, methods=["POST"])
    def login_or_signup(self, request):
        serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            user = authenticate(request, username=username, password=password)

            if user is None:
                raise exceptions.AuthenticationFailed
        else:
            user = User.objects.create_user(username=username, password=password)

        token = SlidingToken.for_user(user)

        response_data = {
            "token": str(token),
            "username": user.username
        }

        response_serializer = AuthenticationResponseSerializer(instance=response_data)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
