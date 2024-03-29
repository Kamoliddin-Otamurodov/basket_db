from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)