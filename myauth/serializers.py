from rest_framework import serializers


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthenticationResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    token = serializers.CharField()
