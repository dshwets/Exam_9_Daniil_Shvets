from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class AddToFavorite(APIView):
    permission_classes = [IsAuthenticated]


class RemoveFromFavorite(APIView):
    permission_classes = [IsAuthenticated]