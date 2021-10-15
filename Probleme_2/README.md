# APP1 — Problème 2 —

```
              _____    _____   _____   _____                      _   
     /\      / ____|  / ____| |_   _| |_   _|                    | |  
    /  \    | (___   | |        | |     | |         __ _   _ __  | |_ 
   / /\ \    \___ \  | |        | |     | |        / _` | | '__| | __|
  / ____ \   ____) | | |____   _| |_   _| |_      | (_| | | |    | |_ 
 /_/    \_\ |_____/   \_____| |_____| |_____|      \__,_| |_|     \__|
```


## Introduction

```
  _                   _               _             _                          
 | |                 | |             | |           | |                         
 | |        ___      | |__    _   _  | |_        __| |   ___        ___    ___ 
 | |       / _ \     | '_ \  | | | | | __|      / _` |  / _ \      / __|  / _ \
 | |____  |  __/     | |_) | | |_| | | |_      | (_| | |  __/     | (__  |  __/
 |______|  \___|     |_.__/   \__,_|  \__|      \__,_|  \___|      \___|  \___|
                                                                               
                                                                               
  _______   _____                     _             _        
 |__   __| |  __ \                   | |           | |
    | |    | |__) |       ___   ___  | |_        __| |   ___ 
    | |    |  ___/       / _ \ / __| | __|      / _` |  / _ \
    | |    | |          |  __/ \__ \ | |_      | (_| | |  __/
    |_|    |_|           \___| |___/  \__|      \__,_|  \___|
                                          
                                          
      _                      _                                                
     | |                    (_)                                               
   __| |   ___   ___   ___   _   _ __     ___   _ __       ___   _   _   _ __ 
  / _` |  / _ \ / __| / __| | | | '_ \   / _ \ | '__|     / __| | | | | | '__|
 | (_| | |  __/ \__ \ \__ \ | | | | | | |  __/ | |        \__ \ | |_| | | |   
  \__,_|  \___| |___/ |___/ |_| |_| |_|  \___| |_|        |___/  \__,_| |_|   
                                                                              
                                                                              
  _              _                               _                   _ 
 | |            | |                             (_)                 | |
 | |   ___      | |_    ___   _ __   _ __ ___    _   _ __     __ _  | |
 | |  / _ \     | __|  / _ \ | '__| | '_ ` _ \  | | | '_ \   / _` | | |
 | | |  __/     | |_  |  __/ | |    | | | | | | | | | | | | | (_| | | |
 |_|  \___|      \__|  \___| |_|    |_| |_| |_| |_| |_| |_|  \__,_| |_|
                                                                       
                                                                       
      _               _                   _                             
     | |             | |                 | |                            
   __| |  _   _      | |_    ___  __  __ | |_    ___        ___   _ __  
  / _` | | | | |     | __|  / _ \ \ \/ / | __|  / _ \      / _ \ | '_ \ 
 | (_| | | |_| |     | |_  |  __/  >  <  | |_  |  __/     |  __/ | | | |
  \__,_|  \__,_|      \__|  \___| /_/\_\  \__|  \___|      \___| |_| |_|
                                                                        
                                                                        
              _____    _____   _____   _____                      _       
     /\      / ____|  / ____| |_   _| |_   _|                    | |      
    /  \    | (___   | |        | |     | |         __ _   _ __  | |_     
   / /\ \    \___ \  | |        | |     | |        / _` | | '__| | __|    
  / ____ \   ____) | | |____   _| |_   _| |_      | (_| | | |    | |_   _ 
 /_/    \_\ |_____/   \_____| |_____| |_____|      \__,_| |_|     \__| ( )
                                                                       |/ 
                                                                          
                                                                         _     
                                                                        (_)    
   ___    ___    _ __ ___    _ __ ___     ___        ___    ___    ___   _     
  / __|  / _ \  | '_ ` _ \  | '_ ` _ \   / _ \      / __|  / _ \  / __| | |    
 | (__  | (_) | | | | | | | | | | | | | |  __/     | (__  |  __/ | (__  | |  _ 
  \___|  \___/  |_| |_| |_| |_| |_| |_|  \___|      \___|  \___|  \___| |_| (_)
                                                                               
                                                                               
```


## Travail demandé (partie obligatoire)

Il est demandé à chaque équipe de réaliser un script recevant en paramètre un
mot (ou une chaîne de caractères entre guillemets) et affichant cette chaîne
sur le terminal en alphabet "ASCII art" comme démontré ci-dessus.

Exemple de lancement du script :

```
$ python3 ASCII_art.py "ASCII art"
              _____    _____   _____   _____                      _   
     /\      / ____|  / ____| |_   _| |_   _|                    | |  
    /  \    | (___   | |        | |     | |         __ _   _ __  | |_ 
   / /\ \    \___ \  | |        | |     | |        / _` | | '__| | __|
  / ____ \   ____) | | |____   _| |_   _| |_      | (_| | | |    | |_ 
 /_/    \_\ |_____/   \_____| |_____| |_____|      \__,_| |_|     \__|


```

Vous trouverez sur votre dépôt le répertoire `fonts` qui contient plusieurs
polices de caractères que vous pouvez utiliser. Dans un premier temps, nous
vous recommandons d'utiliser la police `fonts/big`.

Le programme doit être écrit en Python 3, s'appeler `ASCII_art.py`, et
accepter 0 ou 1 argument.

- Quand un argument est donné, le programme doit afficher son argument en
  ASCII art en utilisant la police `big.tgz`, comme sur l'exemple ci-dessus.
- Quand aucun argument n'est donné, le programme doit afficher un message
  d'aide, qui devra indiquer la manière d'utiliser le programme et les
  objectifs actuellement atteints.

L'utilisation du module `argparse` est autorisée mais n'est pas obligatoire.

**MERCI DE RESPECTER CES CONSIGNES. LE PROGRAMME SERA TESTÉ EN PARTIE
AUTOMATIQUEMENT.**

## Conseils et objectifs intermédiaires

Il peut être difficile de réaliser intégralement le travail demandé du premier
coup. N'hésitez pas à concevoir d'abord une version simplifiée, puis de la
perfectionner progressivement. Voici quelques exemples de fonctionnalités
intermédiaires possibles :

### Un seul caractère

Le script n'affiche que le premier caractère du texte passé en argument :

```
$ python3 ASCII_art.py abc


   __ _ 
  / _` |
 | (_| |
  \__,_|


```

### Texte fixé à l'avance

Le script affiche une chaîne de caractères codée "en dur", par exemple la chaîne `"Ag"` :

```
$ python3 ASCII_art.py
                   
     /\            
    /  \      __ _ 
   / /\ \    / _` |
  / ____ \  | (_| |
 /_/    \_\  \__, |
              __/ |
             |___/ 
```

### Un caractère par ligne

Le script affiche en ASCII art la chaîne passée en argument verticalement, à
raison d'un caractère par ligne :

```
$ python3 ASCII_art.py Objectif
   ____  
  / __ \ 
 | |  | |
 | |  | |
 | |__| |
  \____/ 
         
         
  _     
 | |    
 | |__  
 | '_ \ 
 | |_) |
 |_.__/ 
        
        
    _ 
   (_)
    _ 
   | |
   | |
   | |
  _/ |
 |__/ 
       
       
   ___ 
  / _ \
 |  __/
  \___|
       
       
       
       
   ___ 
  / __|
 | (__ 
  \___|
       
       
  _   
 | |  
 | |_ 
 | __|
 | |_ 
  \__|
      
      
  _ 
 (_)
  _ 
 | |
 | |
 |_|
    
    
   __ 
  / _|
 | |_ 
 |  _|
 | |  
 |_|  


```


## Améliorations optionnelles

Voici une quelques suggestions d'améliorations optionnelles. Cette liste n'est
pas exhaustive et vous êtes encouragés à faire preuve de créativité.


### Spécification d'une police de caractères

Ajouter un argument optionnel `--police=<chainedecaractère>` qui permet
d'indiquer au programme quelle police de caractère utiliser. Vous trouverez
sur votre dépôt Git quelques autres polices dans le répertoire `fonts` (dans
les répertoires `fonts/small`, `fonts/mini` et `fonts/standard`).

Voici un exemple d'appel :

```
$ python3 ASCII_art.py Ag --police=small
    _          
   /_\    __ _ 
  / _ \  / _` |
 /_/ \_\ \__, |
         |___/ 
```

Merci d'indiquer dans le "message d'usage" les polices disponibles; vous
pouvez créer et ajouter vos propres polices.


### Limite de longueur de chaque ligne

Améliorer le programme afin qu'il coupe automatiquement chaque ligne à un
nombre spécifique de caractères (par défaut : 80).

Voici un exemple d'appel :

```
$ python3 ASCII_art.py "Objectif optionnel B"
   ____    _         _                 _     _    __                       _   
  / __ \  | |       (_)               | |   (_)  / _|                     | |  
 | |  | | | |__      _    ___    ___  | |_   _  | |_        ___    _ __   | |_ 
 | |  | | | '_ \    | |  / _ \  / __| | __| | | |  _|      / _ \  | '_ \  | __|
 | |__| | | |_) |   | | |  __/ | (__  | |_  | | | |       | (_) | | |_) | | |_ 
  \____/  |_.__/    | |  \___|  \___|  \__| |_| |_|        \___/  | .__/   \__|
                   _/ |                                           | |          
                  |__/                                            |_|          
  _                                  _       ____  
 (_)                                | |     |  _ \ 
  _    ___    _ __    _ __     ___  | |     | |_) |
 | |  / _ \  | '_ \  | '_ \   / _ \ | |     |  _ < 
 | | | (_) | | | | | | | | | |  __/ | |     | |_) |
 |_|  \___/  |_| |_| |_| |_|  \___| |_|     |____/ 
                                                   
                                                   
```

On pourra également ajouter un argument supplémentaire `--largeur` afin de
modifier la longueur maximale de chaque ligne dans l'appel :

```
$ python3 ASCII_art.py "Objectif optionnel B" --largeur 58
   ____    _         _                 _     _    __     
  / __ \  | |       (_)               | |   (_)  / _|    
 | |  | | | |__      _    ___    ___  | |_   _  | |_     
 | |  | | | '_ \    | |  / _ \  / __| | __| | | |  _|    
 | |__| | | |_) |   | | |  __/ | (__  | |_  | | | |      
  \____/  |_.__/    | |  \___|  \___|  \__| |_| |_|      
                   _/ |                                  
                  |__/                                   
                  _     _                                
                 | |   (_)                               
   ___    _ __   | |_   _    ___    _ __    _ __     ___ 
  / _ \  | '_ \  | __| | |  / _ \  | '_ \  | '_ \   / _ \
 | (_) | | |_) | | |_  | | | (_) | | | | | | | | | |  __/
  \___/  | .__/   \__| |_|  \___/  |_| |_| |_| |_|  \___|
         | |                                                            
         |_|                                                            
  _       ____  
 | |     |  _ \ 
 | |     | |_) |
 | |     |  _ < 
 | |     | |_) |
 |_|     |____/ 


```


Pour les plus motivés, on pourra même ne couper les lignes que sur un espace :

```
$ python3 ASCII_art.py "Objectif optionnel B" --largeur 80

   ____    _         _                 _     _    __ 
  / __ \  | |       (_)               | |   (_)  / _|
 | |  | | | |__      _    ___    ___  | |_   _  | |_ 
 | |  | | | '_ \    | |  / _ \  / __| | __| | | |  _|
 | |__| | | |_) |   | | |  __/ | (__  | |_  | | | |  
  \____/  |_.__/    | |  \___|  \___|  \__| |_| |_|  
                   _/ |                              
                  |__/                               
                  _     _                                  _       ____  
                 | |   (_)                                | |     |  _ \ 
   ___    _ __   | |_   _    ___    _ __    _ __     ___  | |     | |_) |
  / _ \  | '_ \  | __| | |  / _ \  | '_ \  | '_ \   / _ \ | |     |  _ < 
 | (_) | | |_) | | |_  | | | (_) | | | | | | | | | |  __/ | |     | |_) |
  \___/  | .__/   \__| |_|  \___/  |_| |_| |_| |_|  \___| |_|     |____/ 
         | |                                                             
         |_|                                                             
```

(Attention à prendre en compte correctement le cas où un mot seul ne
rentrerait pas sur la ligne.)


### Gestion des caractères accentués

Modifier le programme afin de gérer les caractères accentués. On pourra
utiliser fichier `accents.txt` (qui se trouve dans l'archive `dec-fonts.tgz`).


### Amélioration de l'espacement des lettres

Pour certaines combinaisons de lettres, l'espacement n'est pas esthétique car
il est trop important par rapport à d'autres combinaisons de lettres. Ceci
arrive par exemple avec la chaîne `bj` dans le mot `objet`, que l'on
affiche:

```
   ____    _         _          _   
  / __ \  | |       (_)        | |  
 | |  | | | |__      _    ___  | |_ 
 | |  | | | '_ \    | |  / _ \ | __|
 | |__| | | |_) |   | | |  __/ | |_ 
  \____/  |_.__/    | |  \___|  \__|
                   _/ |             
                  |__/              
```

Le rendu serait plus joli affiché comme suit (on supprime la
colonne vide entre le `b` et le `j`):

```
   ____    _        _          _   
  / __ \  | |      (_)        | |  
 | |  | | | |__     _    ___  | |_ 
 | |  | | | '_ \   | |  / _ \ | __|
 | |__| | | |_) |  | | |  __/ | |_ 
  \____/  |_.__/   | |  \___|  \__|
                  _/ |             
                 |__/              
```

Le rendu est encore meilleur en faisant passer le `j` en dessous du `b`(plus
difficile):

```
   ____    _       _          _   
  / __ \  | |     (_)        | |  
 | |  | | | |__    _    ___  | |_ 
 | |  | | | '_ \  | |  / _ \ | __|
 | |__| | | |_) | | | |  __/ | |_ 
  \____/  |_.__/  | |  \___|  \__|
                 _/ |             
                |__/              
```

Ceci est dû au fait qu'il y a sur chaque ligne au moins trois espaces entre un
caractère non-espace des représentations de `b` et `j`.  Par exemple dans
l'exemple-ci dessous, il y a au minimum trois `x` par ligne. La distance entre
`b` et `j` est donc de 3, alors que la distance entre `e` et `t` est de 1.

```
   ____    _xxxxxxxxx_          _   
  / __ \  | |xxxxxxx(_)        | |  
 | |  | | | |__xxxxxx_    ___  | |_ 
 | |  | | | '_ \xxxx| |  / _ \ | __|
 | |__| | | |_) |xxx| | |  __/ | |_ 
  \____/  |_.__/xxxx| |  \___|  \__|
          xxxxxxxxx_/ |             
          xxxxxxxx|__/              
```

L'étudiant·e motivé·e pourra même essayer de compacter les mots en supprimant
les espaces et fusionnant les caractères communs, comme ci-dessous.

```
   ____  _     _       _   
  / __ \| |   (_)     | |  
 | |  | | |__  _  ___ | |_ 
 | |  | | '_ \| |/ _ \| __|
 | |__| | |_) | |  __/| |_ 
  \____/|_.__/| |\___| \__|
             _/ |          
            |__/           
```
