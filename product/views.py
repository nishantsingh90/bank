from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Bank
from .serializers import BankSerializer
from rest_framework import filters


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class BankAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter)
    queryset = Bank.objects.all()
    serializer_class = BankSerializer