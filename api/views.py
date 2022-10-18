from operator import mod
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

import js2py
from js2py import require
#from .static.js.roslibjs.build import roslib

'''
convertedFunction = js2py.eval_js(readyFunction)

js2py.eval_js('api/static/js/roslibjs/build/roslib.js')()

check_connections=
var ros = new roslibBring.ROSLIB.Ros();
 
// rosbridge websocket server와의 연결을 생성합니다.
ros.connect('ws://0.0.0.0:9090');


ros.on('error', function (error) {
    console.log(error);
    return 'error';
  });
   
  // 정상 연결
  ros.on('connection', function () {
    console.log('Connection made!');
    return 'connected';
  });
   
  // 연결 닫힘
  ros.on('close', function () {
    console.log('Connection closed.');
    return 'connection closed';
  });

convCheckConnection = js2py.eval_js(check_connections)

'''

class QuestionDetail(APIView):
    def get(self, request, format=None):
        #question = models.Question(title="안녕하세요 질문입니다")
        question = models.Question(title="안녕하세요 질문입니다")
        serializer = serializers.QuestionSerializer(question)
        return Response(serializer.data)

class RobotPositionRequest(APIView):
    def get(self, request, format=None):
        #print(convertedFunction(5,4))
        #robot = models.RobotPosition(Robotposition=convertedFunction(5,4))
        connectionStaus = models.RobotPosition(connectionStatus=convCheckConnection())
        #serializer = serializers.RobotSerializer(robot)
        serializer = serializers.RobotSerializer(connectionStaus)
        return Response(serializer.data)