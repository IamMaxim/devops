import datetime

from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request: HttpRequest):
    return render(request, 'index.html', {'current_time': datetime.datetime.now().isoformat()})


@api_view()
def current_time(request):
    return Response({"current_time": datetime.datetime.now().isoformat()})
