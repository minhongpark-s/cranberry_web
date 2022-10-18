from rest_framework import serializers
from .models import Question
from .models import RobotPosition

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotPosition
        fields = '__all__'