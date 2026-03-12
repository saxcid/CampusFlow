from django.contrib import admin

# Register your models here.

from .models import Etudiant, Enseignements, Semestre, Inscriptions, Evaluations

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom', 'email', 'matricule')

@admin.register(Enseignements)
class EnseignementsAdmin(admin.ModelAdmin):
    list_display= ('code','intitule','coefficient')
    search_fields= ('code','intitule')

@admin.register(Semestre)
class Semestre (admin.ModelAdmin):
    list_display= ('annee_universitaire','nom','date_debut','date_fin')
    search_fields = ('annee_universitaire','nom')

class EvaluationsInline (admin.StackedInline):
    model = Evaluations
    extra = 0

@admin.register(Inscriptions)
class InscriptionAdmin(admin.ModelAdmin):
    list_display=('etudiant','enseignement','semestre','date_inscription')
    list_filter= ('semestre',)
    inlines=[EvaluationsInline]
