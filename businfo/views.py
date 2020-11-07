from django.shortcuts import render

#from rest_framework import status
#from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes  # JWT 데코레이터

from .models import *

from rest_framework_xml.renderers import XMLRenderer


import datetime



@api_view(['GET'])
@renderer_classes((XMLRenderer,))
def busarrivalservice(request):
    if request.method == 'GET':
        now = datetime.datetime.now()

        serviceKey = request.GET.get('serviceKey')
        stationId = request.GET.get('stationId')

        query_set = bus.objects.all()
        buslist = []

        for b in query_set:

            datadict = {'flag':'PASS',
            'locationNo1': b.현재위치,
            'locationNo2': "",
            'lowPlate1': 0,
            'lowPlate2': "",
            'plateNo1': b.번호판,
            'plateNo2': "",
            'predictTime1': "29",
            'predictTime2': "",
            'remainSeatCnt1': -1,
            'remainSeatCnt2': "",
            'routeId': b.routeId,
            'staOrder': 33,
            'stationId': stationId
                        }
            buslist.append(datadict)

        msgHeader = {'queryTime' : now.strftime('%Y-%m-%d %H:%M:%S'),
                  'resultCode' : 0,
                  'resultMessage' :'정상적으로 처리되었습니다."'}



        content = {'msgHeader' : msgHeader,
            'msgBody':buslist}

        return Response(content)

@api_view(['GET'])
@renderer_classes((XMLRenderer,))
def busrouteservice(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        serviceKey = request.GET.get('serviceKey')
        routeId = request.GET.get('routeId')

        b = bus.objects.get(routeId=routeId)

        datadict = {'companyId': '4103600',
                    'companyName': "초고속",
                    'companyTel': "031-123-1234",
                    'districtCd': 2,
                    'downFirstTime': "06:30",
                    'downLastTime': "01:00",
                    'endStationId': "121001315",
                    'endStationName': "사당역(중)",
                    'peekAlloc': 10,
                    'regionName': "과천,서울,수원,용인,의왕",
                    'routeId': b.routeId,
                    'routeName': b.버스번호,
                    'routeTypeCd': 11,
                    'routeTypeName': '직행좌석형시내버스',
                    'startMobileNo': 29059,
                    'startStationId': 228001174,
                    'startStationName':'사색의광장',
                    'upFirstTime' : '05:30',
                    'upLastTime':'00:00',
                    'nPeekAlloc':20
                    }

        msgHeader = {'queryTime': now.strftime('%Y-%m-%d %H:%M:%S'),
                     'resultCode': 0,
                     'resultMessage': '정상적으로 처리되었습니다."'}

        content = {'msgHeader': msgHeader,
                   'msgBody': {'busRouteInfoItem':datadict}}
        return Response(content)
