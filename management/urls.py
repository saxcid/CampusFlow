from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EtudiantViewSet, 
                    EnseignementsViewSet,
                    SemestreViewSet, 
                    InscriptionsViewSet, 
                    EvaluationsViewSet,
                    MyTokenObtainPairView)
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register (r'etudiants', EtudiantViewSet)
router.register (r'enseignements',EnseignementsViewSet)
router.register (r'semestres',SemestreViewSet)
router.register (r'inscriptions',InscriptionsViewSet)
router.register (r'evaluations', EvaluationsViewSet)


urlpatterns = [
    path ('api/',include(router.urls)),
    path ('api/token/', MyTokenObtainPairView.as_view(),name= 'token_obtain_pair'),
    path ('api/token/refresh/',TokenRefreshView.as_view(),name= 'token_refresh'),
]