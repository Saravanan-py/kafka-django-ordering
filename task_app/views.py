from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
from .order import order
from .transaction import transaction
from .confirmation import confirmation
from .analytics import analytics
from rest_framework.views import APIView


def home(request):
    return HttpResponse("hello world")


class OrderAPI(APIView):
    def get(self, request, **kwargs):
        result = order()
        return Response(result)


class TransactionAPI(APIView):
    def get(self, request, **kwargs):
        result = transaction()
        return Response(result)


class ConfirmationAPI(APIView):
    def get(self, request, **kwargs):
        result = confirmation()
        return Response(result)


class AnalyticsAPI(APIView):
    def get(self, request, **kwargs):
        result = analytics()
        return Response(result)
