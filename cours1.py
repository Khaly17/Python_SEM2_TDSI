class Personne:
    
    def __init__(self):
        self.nom = "Khaly"
        self.prenom = "DIENG"
        self.age = 25

    def marche(self):
        print("Je suis une personne")

personne = Personne()#On cree un objet personne
#========================================================
#  Heritage
#======================================================== 
class Etudiant(Personne):#On cree un classe Etudiant qui herite de la classe Personne
    def __init__(self):
        super().__init__()#on appelle le constructeur de base ie la classe Personne
etudiant = Etudiant()#On cree un objet etudiant 

print(etudiant.prenom)#DIENG
print(etudiant.marche())#Je suis une personne 

print(Etudiant.__bases__)#Personne 
print(isinstance(personne,Etudiant))#False
print(isinstance(etudiant,Etudiant))#True
