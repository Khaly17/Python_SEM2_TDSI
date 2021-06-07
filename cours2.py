class Personne:

    #constructeur
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    #Cette methode gere l'affichage des chaines
    def __str__(self):
        return "<class,'Personne'>"
    
    def __add__(self,personne):
        return self.nom+" "+self.prenom,personne.nom+" "+personne.prenom

    #Cette meethode renvoie True si 
    # les deux noms sont identiques et False sinon 
    def __eq__(self, personne):
        return self.nom==personne.nom

    #cette methode gere <= pour les chaine
    def __le__(self, personne):
        return self.nom<=personne.nom

    def __repr__(self):
         return "I am a coder"
    
       
#instanciation deux objets personnes
personne1 = Personne("Sall","Issa",35)
personne2 = Personne("FAll","Arame",25)

print(personne1+personne2)
print(personne1<=personne2)





