from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from api.serializers import UserSerializer
from api.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# @api_view(['GET'])
# def user_list(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def user_detail(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)


@api_view(['GET'])
def test(request):
    response = {
        "message": "Test OK"
    }
    return Response(response)