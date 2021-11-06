import math


class Vecteur:
    def __init__(self, x: float = 0., y: float = 0.) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vecteur") -> "Vecteur":
        return Vecteur(self.x + other.x, self.y + other.y)

    def __mul__(self, other: float) -> "Vecteur":
        return Vecteur(other * self.x, other * self.y)

    def distance_carre(first: "Vecteur", second: "Vecteur") -> float:
        return (first.x - second.x)**2 + (first.y - second.y)**2

    def __repr__(self) -> str:
        return 'Vecteur({}, {})'.format(self.x, self.y)

if __name__ == '__main__':
    vecteur1 = Vecteur(2, 4)
    vecteur2 = Vecteur(4, 3)

    vecteur2 += vecteur1
    print(vecteur2)
