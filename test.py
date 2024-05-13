import random

# # Hello, world
# print('Bonjour,')

# # Dictionnaire
# dic = {
#     'id' : 1,
#     'nom' : 'Yazid',
#     'prenom' : 'Said',
#     'age' : 15,
#     'villes' : {'Paris','Lyon'},
#     'notes' : [10,12,8,7]
# }

# print(dic)
# for key in dic:
#     print(dic[key]) # Affiche seulement les valeurs du dictionnaire.

# for key in dic:
#     print(key) # Affiche seulement les clés du dictionnaire.

# print(dic['nom']) # Affiche la valeur du clé nom

# # boucle FOR pour les notes du dictionnaires.. (list)
# for note in dic['notes']:
#     print(note)

# random.randint(a, b)
def rad(max):
    a = random.randint(0, max)
    b = random.randint(0, max)
    obj = {'n1' : a,'n2' : b, 'somme' : a+b}
    return "La somme de ", obj["n1"]," et ", obj["n2"]," est ", obj["somme"]

print(rad(10))

#####
couleur = ["bleu","jaune","blanche","rouge","vert","#00FFFF"]

print(random.choice(couleur)) # Choisir un élement au hasard d'une séquence(liste)

def aleatoire(bool,list1,min,max): 
    if(bool==True):
        return random.choice(list1)
    else:
        return "Somme est ", random.randint(min,max)

print(aleatoire(False,[1,25,6,7],0,50))