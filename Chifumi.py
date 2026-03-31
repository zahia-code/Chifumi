import random

def jeuduchifumi():
     print("--- Jeu du chifumi ---")
     options = ["pierre", "feuille", "ciseaux"]
     
     choix_ordi = random.choice(options)
     choix_joueur = input("Pierre, Feuille ou Ciseaux ?").lower()
      
     if choix_joueur == choix_ordi:
         print("Égalité!")
     elif choix_joueur == "pierre" and choix_ordi == "ciseaux":
        print("Gagné ! La pierre écrase les ciseaux.")
     elif choix_joueur == "feuille" and choix_ordi == "pierre":
        print("Gagné ! La feuille enveloppe la pierre.")
     elif choix_joueur == "ciseaux" and choix_ordi == "feuille":
        print("Gagné ! Les ciseaux coupent la feuille.")
     else:
        print("Perdu ! Retente ta chance.")
        
jeuduchifumi()
