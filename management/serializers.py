from rest_framework import serializers

from .models import (Etudiant
                     ,Enseignements
                     ,Semestre
                     ,Inscriptions
                     , Evaluations)
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['is_staff'] = self.user.is_staff
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model= Etudiant
        fields= '__all__'

class EnseignementsSerializer (serializers.ModelSerializer):

    class Meta:
        model= Enseignements
        fields ='__all__'

class SemestreSerializer (serializers.ModelSerializer):

    class Meta:
        model= Semestre
        fields = '__all__'

class InscriptionsSerializer (serializers.ModelSerializer):
    
    class Meta:
        model= Inscriptions
        fields ='__all__'

class EvaluationsSerializer (serializers.ModelSerializer):

    class Meta:
        model= Evaluations
        fields ='__all__'
