from django.db import models

# Create your models here.

class Etudiant (models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Enseignements (models.Model):
    code = models.CharField(max_length=100, unique=True)
    intitule = models.CharField(max_length=100)
    coefficient = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.code}-{self.intitule}"

class Semestre (models.Model):
    annee_universitaire = models.CharField(max_length=9)
    nom = models.CharField(max_length=2)
    date_debut = models.DateField()
    date_fin = models.DateField()

    class Meta :
        unique_together = ('annee_universitaire', 'nom')
    
    def __str__(self):
        return f"{self.nom}-{self.annee_universitaire}"
    
class Inscriptions (models.Model):
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    enseignement= models.ForeignKey(Enseignements, on_delete=models.CASCADE)
    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)

    class Meta :
        unique_together = ('etudiant','enseignement','semestre')
    
    def __str__(self):
        return f"{self.etudiant},{self.enseignement} ,{self.semestre}"

class Evaluations (models.Model):
    inscriptions= models.ForeignKey(Inscriptions, on_delete=models.CASCADE, related_name='evaluation')
    note = models.DecimalField (max_digits=4,decimal_places=1)
    date_evaluation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Inscriptions}:{self.note}"
    
