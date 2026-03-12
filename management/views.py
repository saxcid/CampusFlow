from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from .models import (Etudiant,
                     Enseignements,
                     Semestre,
                     Inscriptions,
                     Evaluations)
from .serializers import (EtudiantSerializer,
                          EnseignementsSerializer, 
                          SemestreSerializer,
                          InscriptionsSerializer,
                          EvaluationsSerializer,
                          UserSerializer,
                          MyTokenObtainPairSerializer,
                          User)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAdminUser]

class EtudiantViewSet (viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nom','prenom','matricule']
    permissions_classes = [IsAuthenticatedOrReadOnly]


class EnseignementsViewSet(viewsets.ModelViewSet):
    queryset = Enseignements.objects.all()
    serializer_class= EnseignementsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code','intitule']
    permissions_classes = [IsAuthenticatedOrReadOnly]

class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    serializer_class= SemestreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nom','date_debut']
    permissions_classes = [IsAuthenticatedOrReadOnly]

class InscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Inscriptions.objects.all()
    serializer_class= InscriptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['etudiant','enseignement','semestre']
    permissions_classes = [IsAdminUser]

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['note','inscriptions']
    permissions_classes = [IsAdminUser]


