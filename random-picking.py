import math

def calculer_probabilite(k, nb_rouge, nb_blanche, nb_noire):
    # Vérifier que les paramètres sont valides
    if k < 3 or nb_rouge < 1 or nb_blanche < 1 or nb_noire < 1:
        raise ValueError("Les paramètres doivent être valides.")

    # Calculer le nombre total de boules dans l'urne
    total_boules = nb_rouge + nb_blanche + nb_noire

    # Vérifier que le nombre de boules à tirer est inférieur ou égal au nombre total de boules
    if k > total_boules:
        raise ValueError("Le nombre de boules à tirer ne peut pas dépasser le nombre total de boules.")

    # Calculer le nombre de façons de choisir une boule de chaque couleur
    facons_choisir_une_boule = math.comb(nb_rouge, 1) * math.comb(nb_blanche, 1) * math.comb(nb_noire, 1)

    # Calculer le nombre total de façons de choisir k boules parmi toutes les boules
    facons_choisir_k_boules = math.comb(total_boules, k)

    # Calculer la probabilité d'obtenir exactement une boule de chaque couleur
    probabilite = facons_choisir_une_boule / facons_choisir_k_boules

    return probabilite

# Exemple d'utilisation de la fonction
k = 3  # Nombre total de boules à tirer
nb_rouge = 4  # Nombre de boules rouges
nb_blanche = 3  # Nombre de boules blanches
nb_noire = 2  # Nombre de boules noires

probabilite = calculer_probabilite(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité d'obtenir exactement une boule de chaque couleur est : {probabilite:.2f}")
