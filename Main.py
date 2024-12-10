# Titre : Programme simple d'aide à la mutation à l'automate
# Date de création : 21-11-2024
# Auteur : Calvin Nd.

# Espacement pour lisibilité
print ("  ")

# Espacement pour titre
print ("-- Bienvenue sur l'outil d'aide à la mutation automate --")
print ("                    Créé par Calvin                      ")
print ("                    N°version : 2.0                      ")

# Espacement pour lisibilité
print ("  ")

# Zone de saisie avec try/catch
while True:
    try:
        hauteur = int(input("> Veuillez indiquer la hauteur du produit (en mm) : "))
        break
    except ValueError:
        print("> Syntaxe invalide. Ce n'est pas un nombre valide. Réessayer.")
        # Espacement pour lisibilité
        print("  ")

while True:
    try:
        moyenne = int(input("> Veuillez indiquer la moyenne de vente (par mois) : "))
        break
    except ValueError:
        print("> Syntaxe invalide. Ce n'est pas un nombre valide. Réessayer.")
        # Espacement pour lisibilité
        print("  ")

while True:
    try:
        frequence = int(input("> Veuillez indiquer la fréquence picking mensuel (M-1) : "))
        break
    except ValueError:
        print("> Syntaxe invalide. Ce n'est pas un nombre valide. Réessayer.")
        # Espacement pour lisibilité
        print("  ")

while True:
    try:
        hauteurG = int(input("> Veuillez indiquer la hauteur du canaux désiré à l'automate (mm) : "))
        break
    except ValueError:
        print("> Syntaxe invalide. Ce n'est pas un nombre valide. Réessayer.")
        # Espacement pour lisibilité
        print("  ")

# Fonction de détermination de la zone du produit correspondant
def zone():

# Condition fréquence minimum 60 et condition picking
    if frequence > 60 and NBC < 5 and NbGoulotte < 3.2:
        reponse = True
    else:
        reponse = False
    return reponse

# Calculs des informations à partir des relevés INT040

# Nombre de boîtes vendues par jour
NBV = moyenne/25

# Hauteur totale nécessaire en mm par jour
HT = hauteur * NBV

# Nombre de goulottes nécessaire de 800
NbGoulotte = HT/hauteurG

# Nombre de boîtes par commande
NBC = moyenne / frequence

# Espacement pour lisibilité
print ("  ")
print ("  ")

# Zone de résultat
print(" -- Relevé d'informations concernant votre produit --  ")
print ("  ")
print("> Nombre de boîtes vendues (par jour) : ", round(NBV))
print("> Hauteur totale nécessaire (par jour) : ", round(HT),"mm")
print("> Nombre de canaux de", hauteurG,"mm","nécessaire (par jour) : ", round(NbGoulotte, 2))
print("> Nombre de boîte par commande (en moyenne) : ", round(NBC))

# Espacement pour lisibilité et titre
print ("  ")
print(" -- Conclusions --  ")
print ("  ")

if NBC < 5 and NbGoulotte < 3.2:
    # Réponse et détermination du type de canaux (taille)
    if NbGoulotte > 1.2:
        print("> Dans cette configuration, il serait souhaitable d'opter pour une hauteur de canaux plus grande.")
        print("> Sinon, il faudrait mettre en place", round(NbGoulotte, 1), "canaux de", hauteurG, "mm.")
    else:
        pourcentage = NbGoulotte * 100
        print("> Parfait pour cette configuration en terme de hauteur de canaux, ce produit nécessitera précisement",
              round(pourcentage, 1), "% d'un canaux de", hauteurG, "mm.")

# Définition de la zone
if zone():
    print("  ") # Espacement pour lisibilité
    print("> Ce produit peut aller à l'automate.")
else:
    print("> Ce produit doit aller au magasin. Il n'est pas compatible avec les exigences de l'automate.")