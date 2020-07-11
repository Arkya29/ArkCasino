# -*-coding:Latin-1 -*
from random import randrange
from math import ceil
from time import sleep

print("\n+-----------ArkCasino-----------+")

# On verifie et demande qu'une somme d'agent positive (à convertir en crédit) soit entrée sous forme de nombre entier, en chiffre(s).
argent = -1
argent = int(argent)
while argent < 0 or argent >= 1000000000:
    argent = input("\nQuelle somme d'agent voulez-vous convertir en crédits ?")
    try:  # On vérifie que le joueur a bien saisi une somme d'argent en chiffres.
        argent = int(argent)
    except:
        print(
            "- ERREUR : Merci de renseigner la somme d'argent, supérieure à 0, sous forme nombre entier et de chiffres.")
        argent = -1
        continue
    argent = int(argent)
    if argent < 1:  # On vérifie que le joueur saisi une somme positive.
        print("- ERREUR : Veuillez saisir un nombre entier positif.")
        argent = -1
    if argent >= 1000000000:  # On vérifie que le joueur saisi une somme inférieure à un milliard.
        print(
            "- ERREUR : Afin de limiter la fraude, veuillez convertir moins d'un milliard (1 000 000 000) de dollards à la fois.")
credit = argent
credit = int(credit)
print("Vous avez bien converti", argent, "$ en", credit, "crédits. 1 crédit = 1$")  # Bilan de la conversion.

continuer = True
while continuer:
    # On demande la somme que le joueur veut miser pour cette manche.
    # Puis on regarde si le joueur a misé un nombre correct de crédits.
    print("\nVous avez", credit, "crédits.")
    mise = 1000000001
    mise = int(mise)
    while mise > credit:
        mise = input("Combien de crédits voulez-vous miser pour cette manche ?")
        try:
            mise = int(mise)  # On vérifie que le joueur a bien saisi une somme en chiffres.
        except:
            print("- ERREUR : Merci de saisir la somme de crédit misée en chiffres et nombre entier.\n")
            mise = 1000000000
            continue
        mise = int(mise)
        if mise > credit:  # On vérifie que le joueur ne mise pas plus qu'il a d'argent.
            print("Vous avez seulement", credit, "crédits.\n")

    # Bilan des crédits misés et restants
    credit = credit - mise
    print("Vous avez misé", mise, "crédits pour cette manche. Il vous reste", credit, "crédits.\n")

    # On débute le jeu
    # On demande un numéro sur lequel miser et on vérifie qu'il est correct.
    numero = -1
    numero = int(numero)
    while numero < 0 or numero > 49:
        numero = input("Sur quel numéro entre 0 et 49 compris voulez-vous miser ?")
        try:  # On vérifie que le joueur a bien saisi un nombre en chiffres.
            numero = int(numero)
        except:
            print("- ERREUR : Merci de saisir le numéro choisi en chiffres.\n")
            numero = -1
            continue
        if numero < 0 or numero > 49:  #  On vérifie que le joueur a bien saisi un nombre entre 0 et 49 compris.
            print("- ERREUR : Merci de un numéro entre 0 et 49 compris.\n")

    # On définie une couleur à ce numéro.
    couleur = numero % 2  # Reste du numéro (si 0 -> pair, si 1 -> impaire).
    couleur = int(couleur)
    if couleur == 0:  # Si la nombre est pair (noir).
        couleur = "noir"
    if couleur == 1:  # Si le nombre est impair (rouge).
        couleur = "rouge"

    # Bilan du numéro / couleur misé.
    print("Vous avez misé sur le numéro", numero, ", de couleur", couleur, ".\n")

    # On fait tourner la roue et on dit quels est le numéro/coueleur tiré.
    print("La roue tourne...\n")
    sleep(3)
    numeror = randrange(59)  # numeror = numéro tiré et couleurr = couleur tirée.
    if numeror % 2 == 0:  # Si numeror est pair
        couleurr = "noir"
    if numeror % 2 == 1:  # Si numeror est impair.
        couleurr = "rouge"
    print("La bille s'arrête sur le numéro", numeror, "de couleur", couleurr, ".")

    # On détermine les gains du joueur.
    gains = 0
    gains = int(gains)
    if numero == numeror:  # Si la bille s'arrête sur le bon numéro.
        print("La bille s'est arrêtée sur le numéro sur lequel vous avez misé ! Vous gagnez trois fois votre mise !")
        gains = + mise * 3
    if numero != numeror and couleur == couleurr:  # Si la bille s'arrête sur la bonne couleur, mais pas sur le bon numéro.
        print(
            "La bille ne s'est pas arrêtée sur le numéro sur lequel vous avez misé, mais sur la bonne couleur ! Vous gagnez la moitié de votre mise.")
        gains = ceil(mise / 2)
    if couleur != couleurr:  # Si la bille ne s'arrête ni sur le bon numéro, ni sur la bonne couleur.
        print(
            "La bille ne s'est pas arrêtée sur le numéro sur lequel vous avez misé, ni sur la bonne couleur. Vous perdez toute votre mise.")

    print("Vous avez misé", mise, "$, et vous avez gagné", gains, "$.")  # Bilan de la partie.
    credit = credit + gains  # On ajoute les gains aux crédits.
    print("Vous avez maintenant", credit, "crédits.")  # Bilan des crédits restants.

    replay = "?"
    sleep(3)
    if credit <= 0:  # Si on a plus d'argent, quitter la partie.
        print("Vous êtes ruinés, et nous riches MOUHAHA ! Vous quittez le jeu avec 0$ en poche.")
        continuer = False
        break
    while replay != "Oui" or replay != "oui" or replay != "Non" or replay != "non":
        replay = input("\nVoulez-vous rejouer [Oui] ou [Non] ?")
        if replay == "Oui" or replay == "oui" or replay == "OUI":  # Si on le souhaite, ne pas quitter la partie.
            print("Relancement de la partie...")
            sleep(1)
            continuer = True
            break
        elif replay == "Non" or replay == "non" or replay == "NON":  # Si on le souhaite, quitter la partie.
            print("Vous quittez le jeu avec", credit, "$ en poche.")
            replay = "Non"
            continuer = False
            break
        else:  # Demander à la personne de tapper "Oui" ou "Non", et pas autre chose.
            print("Merci de taper \"Oui\" ou \"Non\"")

input("\nAppuyez sur la touche \"Entrer\" pour fermer le programme.")  # On ferme le programme.
