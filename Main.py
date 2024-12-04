# Titre : Programme simple d'aide à la mutation à l'automate
# Date : 21-11-2024
# Auteur : Calvin Nd.

# Espacement pour lisibilité
print ("  ")

# Espacement pour titre
print ("-- Bienvenue sur l'outil d'aide à la mutation automate --")
print ("                    Créé par Calvin                      ")
print ("                    N°version : 1.0                      ")

# Espacement pour lisibilité
print ("  ")

# Zone de saisie
hauteur = int(input("Veuillez indiquer la hauteur du produit (en mm) : "))
moyenne = int(input("Veuillez indiquer la moyenne de vente par mois : "))
frequence = int(input("Veuillez indiquer la fréquence : "))
hauteurG = int(input("Veuillez indiquer la hauteur de la goulotte désirée (mm) : "))

# Fonction de détermination de la zone du produit correspondant
def zone():

# Condition fréquence minimum 60 et condition picking
    if frequence > 60 and NBC < 5 and hauteurG < 3.2:
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
print("Nombre de boîtes vendues par jour : ", round(NBV))
print("Hauteur totale nécessaire : ", round(HT),"mm")
print ("Nombre de goulotte de", hauteurG,"mm","nécessaire : ", round(NbGoulotte, 1))
print("Nombre de boîte par commande : ", round(NBC))

# Espacement pour lisibilité et titre
print ("  ")
print(" -- Conclusions --  ")
print ("  ")

if NBC < 5 and hauteurG < 3.2:
    # Réponse et détermination du type de canaux (taille)
    if NbGoulotte > 1.2:
        print("Ce produit devrait aller dans une goulotte plus grande.", hauteurG, "mm, ne suffira probablement pas.")
        print("Il faudrait sinon mettre en place", round(NbGoulotte, 1), "canaux")
    else:
        pourcentage = NbGoulotte * 100
        print("Parfait pour cette configuration en terme de taille de goulotte, ce produit nécessitera précisement",
              round(pourcentage, 1), "% d'une goulotte de", hauteurG, "mm.")


# Définition de la zone
if zone():
    print("  ") # Espacement pour lisibilité
    print("Ce produit peut aller à l'automate.")
else:
    print("Ce produit doit aller au magasin. Il n'est pas compatible avec les exigences de l'automate.")

# Espacement pour lisibilité
print ("  ")