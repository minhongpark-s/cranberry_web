from django.shortcuts import render, redirect

import json
from django.http import HttpResponse
from django.http import JsonResponse

from .models import robotData
from datetime import datetime
from time import sleep
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def dashboard(request):
    return render(
                request,
                'dashboard/index.html',
                 )

def robotPositionRequest(request):
    return render(
                request,
                'dashboard/index.html', # make waiting process.
    )


def topicConnectionTest(request):
    return render(
        request,
        'dashboard/topicConnectionTest.html',
    )

def jsonTest(request):
    #return JsonResponse({'foo':'bar'})
    return 


def databaseTest(request):
    return render(
        request,
        'dashboard/databaseTest.html',
    )

def robotDataCleanUp(request):
    q = robotData.objects.all()
    q.delete()
    return redirect('databaseTest')

@csrf_exempt
def updateDatabase(request):
    if request.method == 'GET':
        rd = robotData()
        rd.robotPositionY = int(request.GET.get('x'))
        rd.robotPositionX = int(request.GET.get('y'))
        rd.checked_at = datetime.now()
        rd.save()
        #return redirect('databaseTest')
        return render(
            request,
            'dashboard/databaseTestSecond.html',
        )
    if request.method == 'POST':
        receive_message_x = request.POST.get('x')
        receive_message_y = request.POST.get('y')
        rd = robotData()
        rd.robotPositionY = int(receive_message_x)
        rd.robotPositionX = int(receive_message_y)
        rd.checked_at = datetime.now()
        rd.save()
        send_message = {'send_data' : "I received "+ receive_message_x + " and " + receive_message_y}
        return JsonResponse(send_message)

@csrf_exempt
def ajax_method(request):
    receive_message = request.POST.get('x')
    send_message = {'send_data' : "I received "+receive_message}
    return JsonResponse(send_message)