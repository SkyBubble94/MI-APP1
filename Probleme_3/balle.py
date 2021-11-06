import fltk
from constantes import LARGEUR, HAUTEUR
from vecteur import Vecteur
from random import uniform

class Balle:
    def __init__(self, rayon: int = 20, position: Vecteur = Vecteur(), vitesse: Vecteur = Vecteur(), couleur: str = 'black') -> None:
        self.rayon = rayon
        self.position = position
        self.vitesse = vitesse
        self.couleur = couleur

    def dessine(self) -> None:
        fltk.cercle(self.position.x, self.position.y, self.rayon, "black", self.couleur)

    def deplace(self, end = False) -> None:
        if (self.position.x >= LARGEUR - self.rayon or self.position.x <= 0 + self.rayon):
            self.vitesse.x = -self.vitesse.x
        if not end and (self.position.y >= HAUTEUR - self.rayon or self.position.y <= 0 + self.rayon):
            self.vitesse.y = -self.vitesse.y
        self.position += self.vitesse


class BalleRouge(Balle):
    def __init__(self, rayon = 20) -> None:
        position = Vecteur(uniform(rayon, LARGEUR - rayon), uniform(rayon, HAUTEUR - rayon))
        vitesse = Vecteur(uniform(-5, 5), uniform(-5, 5))
        couleur = 'red'
        super().__init__(rayon, position, vitesse, couleur)


class Joueur(Balle):
    def __init__(self, rayon=20) -> None:
        rayon = rayon
        position = Vecteur(fltk.abscisse_souris(), fltk.ordonnee_souris())
        vitesse = Vecteur()
        couleur = "blue"
        super().__init__(rayon, position, vitesse, couleur)
    
    def suis_souris(self) -> None:
        if self.rayon >= fltk.ordonnee_souris():
            self.position.y = self.rayon
        elif fltk.ordonnee_souris() >= HAUTEUR - self.rayon:
            self.position.y = HAUTEUR - self.rayon
        else:
            self.position.y = fltk.ordonnee_souris()
        if self.rayon >= fltk.abscisse_souris():
            self.position.x = self.rayon
        elif fltk.abscisse_souris() >= LARGEUR - self.rayon:
            self.position.x = LARGEUR - self.rayon
        else:
            self.position.x = fltk.abscisse_souris()
