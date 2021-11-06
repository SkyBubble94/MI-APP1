import argparse
import fltk
import time
from vecteur import Vecteur
from balle import BalleRouge, Joueur
from constantes import LARGEUR, HAUTEUR
from itertools import combinations

MENU = 0
INIT = 1
JEU = 2
FIN = 3
FERME = 4

def scene() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nb_boules', type=int, default=4, help="Nombre de boules")
    parser.add_argument('-r', '--rayon_boules', type=int, default=20, help="Rayon des boules")
    parser.add_argument('-m', '--mode', type=str, default='gazeux', choices=['gazeux', 'solide'], help="Mode de jeux")
    args = parser.parse_args()

    fltk.cree_fenetre(LARGEUR, LARGEUR, 60)
    temps = None
    etat = MENU
    while True:
        while etat is MENU:
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            if tev == "Quitte":
                etat = FERME
            if tev == "ClicGauche":
                etat = INIT

            fltk.efface_tout()
            if temps is None:
                fltk.texte(LARGEUR//2, HAUTEUR//2, 'Cliquez pour commencer', ancrage='center')
            else:
                fltk.texte(LARGEUR//2, HAUTEUR//2, f'Temps : {temps} secondes\nCliquez pour recommencer', ancrage='center')
            fltk.mise_a_jour()

        if etat is INIT:            
            joueur = Joueur(rayon=args.rayon_boules)
            balles = []
            for _ in range(args.nb_boules):
                balle = BalleRouge(rayon=args.rayon_boules)
                valide = False
                while not valide:
                    if not any(Vecteur.distance_carre(balle.position, autre_balle.position) < (balle.rayon + autre_balle.rayon)**2 for autre_balle in balles):
                        balles.append(balle)
                        break
                    balle = BalleRouge(rayon=args.rayon_boules)

            for _ in range(120):
                fltk.efface_tout()
                joueur.suis_souris()
                joueur.dessine()
                for balle in balles:
                    balle.dessine()
                fltk.mise_a_jour()
            
            debut = time.time()
            etat = JEU
        
        while etat is JEU:
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            if tev == "Quitte":
                etat = FERME
            
            fltk.efface_tout()
            if int(time.time() - debut) <= 1:
                chrono = f"{int(time.time() - debut)} seconde"
            else:
                chrono = f"{int(time.time() - debut)} secondes"
            fltk.texte(10, 10, chrono)
            
            if int(time.time() - debut) // 30 > len(balles) - args.nb_boules:
                balle = BalleRouge(rayon=args.rayon_boules)
                if not any(Vecteur.distance_carre(balle.position, autre_balle.position) < (balle.rayon + autre_balle.rayon)**2 for autre_balle in (*balles, joueur)):
                    balles.append(balle)


            joueur.suis_souris()
            joueur.dessine()
            if args.mode == 'solide':
                for balle, autre_balle in combinations(balles, 2):
                    if Vecteur.distance_carre(balle.position, autre_balle.position) <= (balle.rayon + autre_balle.rayon)**2:
                        vitesse_autre = autre_balle.vitesse
                        autre_balle.vitesse = balle.vitesse
                        balle.vitesse = vitesse_autre
            for balle in balles:
                balle.deplace()
                balle.dessine()
                if Vecteur.distance_carre(balle.position, joueur.position) <= (balle.rayon + joueur.rayon)**2:
                    etat = FIN

            fltk.mise_a_jour()

        if etat is FIN:
            balles.append(joueur) # le joueur devient une balle quelconque
            temps = int(time.time() - debut)
            while any(True for balle in balles if balle.position.y < HAUTEUR + 2 * balle.rayon):  # tant que toutes les balles sont visibles
                ev = fltk.donne_ev()
                tev = fltk.type_ev(ev)

                if tev == "Quitte":
                    etat = FERME
                    break

                fltk.efface_tout()
                fltk.texte(10, 10, chrono)
                for balle in balles:
                    balle.vitesse.y += 1
                    balle.deplace(True)
                    for autre_balle in balles:
                        if autre_balle == balle:
                            continue
                        if args.mode == 'solide':
                            if Vecteur.distance_carre(balle.position, autre_balle.position) <= (balle.rayon + autre_balle.rayon)**2:
                                vitesse_autre = autre_balle.vitesse
                                autre_balle.vitesse = balle.vitesse
                                balle.vitesse = vitesse_autre
                    balle.dessine()

                fltk.mise_a_jour()
            etat = MENU

        if etat is FERME:
            break

if __name__ == '__main__':
    scene()
