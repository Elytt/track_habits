### import zone ###
import json
import os
from datetime import datetime
import calendar

FICHIER_DONNEES = "tracker_data.json"

# --- GESTION DES DONNÉES ---
def charger_donnees():
    if os.path.exists(FICHIER_DONNEES):
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            return json.load(f)
    # Structure de base si le fichier n'existe pas
    return {
        "Travail": [],
        "Sport": [],
        "Études": {
            "Revisions aujourd'hui": [],
            "Prochain examen": "Non défini",
            "Prochain cours": "Non défini"
        }
    }

def sauvegarder_donnees(donnees):
    with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

# --- AFFICHAGE ---
def afficher_calendrier():
    maintenant = datetime.now()
    print("\n" + "="*30)
    print(" CALENDRIER DU MOIS")
    print("="*30)
    # Affiche le calendrier du mois en cours
    print(calendar.month(maintenant.year, maintenant.month))

def afficher_etat(donnees):
    print("\n" + "="*30)
    print("📊 TON HABIT TRACKER")
    print("="*30)
    print("\nTRAVAIL :")
    for hab in donnees["Travail"]:
        print(f"  - {hab}")
    print("\n SPORT :")
    for hab in donnees["Sport"]:
        print(f"  - {hab}")
    print("\n ÉTUDES :")
    print("  ➤ Révisions aujourd'hui :")
    for rev in donnees["Études"]["Revisions aujourd'hui"]:
        print(f"    - {rev}")
    print(f"  ➤ Prochain examen : {donnees['Études']['Prochain examen']}")
    print(f"  ➤ Prochain cours  : {donnees['Études']['Prochain cours']}")
    print("="*30)

# --- MENU PRINCIPAL ---
def menu():
    donnees = charger_donnees()
    while True:
        print("\n--- MENU ---")
        print("1. Voir mon Tracker")
        print("2. Voir le Calendrier")
        print("3. Ajouter une habitude (Travail / Sport)")
        print("4. Mettre à jour les Études")
        print("5. Quitter")
        choix = input("Choisis une option (1-5) : ")
        if choix == "1":
            afficher_etat(donnees)
        elif choix == "2":
            afficher_calendrier()
        elif choix == "3":
            cat = input("Catégorie (1 pour Travail, 2 pour Sport) : ")
            nom = input("Nom de l'habitude : ")
            if cat == "1":
                donnees["Travail"].append(nom)
            elif cat == "2":
                donnees["Sport"].append(nom)
            sauvegarder_donnees(donnees)
            print("Habitude ajoutée !")
        elif choix == "4":
            print("1. Ajouter une révision pour aujourd'hui")
            print("2. Modifier la date du prochain examen")
            print("3. Modifier la date du prochain cours")
            sous_choix = input("Ton choix (1-3) : ")
            if sous_choix == "1":
                rev = input("Quoi réviser ? : ")
                donnees["Études"]["Revisions aujourd'hui"].append(rev)
            elif sous_choix == "2":
                date_ex = input("Date ou nom du prochain examen : ")
                donnees["Études"]["Prochain examen"] = date_ex
            elif sous_choix == "3":
                date_cours = input("Date ou nom du prochain cours : ")
                donnees["Études"]["Prochain cours"] = date_cours
            sauvegarder_donnees(donnees)
            print("Études mises à jour !")
        elif choix == "5":
            print("À bientôt ! Continue sur ta lancée ! ")
            break
        else:
            print("❌ Option invalide, réessaie.")

if __name__ == "__main__":
    menu()
