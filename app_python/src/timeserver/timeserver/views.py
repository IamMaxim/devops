import datetime

from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request: HttpRequest):
    visits = 0
    try:
        with open("/volume/visits", 'r') as f:
            visits = int(f.readline()) + 1
            print(visits)
    except:
        pass
    try:
        with open("/volume/visits", 'w') as f:
            f.write(str(visits))
    except:
        pass

    return render(request, 'index.html', {
        'current_time': datetime.datetime.now(datetime.timezone.utc).isoformat()
    })


@api_view()
def current_time(request):
    return Response({
        "current_time": datetime.datetime.now(datetime.timezone.utc).isoformat()
    })


def visits(request: HttpRequest):
    with open('/volume/visits', 'r') as f:
        visits = f.readline()

    return render(request, 'visits.html', {
        'visits': visits
    })
