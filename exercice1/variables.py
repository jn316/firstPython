def calcul_per(longueur, largeur):
    perimetre = longueur * largeur
    print('la longueur {} et la largeur {} donne le perimetre {}'.format(longueur, largeur, perimetre))
    
def main():
    print('debut du programme')
    calcul_per(2,4)

if __name__ == '__main__' : main()