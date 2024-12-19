import time



def countdown(n):
    """
    Génère un compte à rebours de 1 à n et retourne la durée d'exécution.

    n: un entier qui représente le nombre de secondes du compte à rebours.

    """
    

    # Générer la séquence de nombres avec une temporisation de 1 seconde
    for i in range(n):

        start_time = time.perf_counter()  # Enregistre l'heure de début
        time.sleep(t)  # Attendre 1 seconde
        end_time = time.perf_counter()  # Enregistre l'heure de fin
        duration = end_time - start_time  # Calcule la durée d'exécution

        print(i)  # Afficher le nombre et remplacer le caractère de fin de ligne par un retour à la ligne
        
        
        print(f"\nDurée d'exécution : {duration:.2f} secondes")
    
    



if __name__ == '__main__':
    n = int(input("Entrez la valeur de N: "))
    t = float(input("Voulez-vous afficher le temps d'exécuton ? : "))
    countdown(n)

