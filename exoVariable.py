
#----------------------------------- exo 1------------------------------------------------------
# Print une phrase dynamique (dynamique = avec des données changeante)
# "je suis PRENOM, j'habite a VILLE et j'ai AGE ans"
# prenom, ville et age seront dans des variables
name = "Sandrine"
city = "Brésil"
age = 24
print(f"je suis {name}, j'habite a {city} et j'ai {age} ans")

#-------------------------------------- Exo 2-----------------------------------------------------
# Print une phrase "le total est de TOTAL euros"
# vous avez acheté une baguette et un croissant
# le montant de ces articles sont dans des variables
baguette = 1
croissant = 2
total = baguette + croissant
print(f"le total est de {total} euros")

# Exo3 
# Lors d'un jeu vous avez dix points
# Faire un print de vos points 
# Au premier tour vous perdez 1 pts
# au deuxieme tour vous en gagnez 5
# au dernier tour vous en perdez la moitié
# faire un print de votre nouveau total de points a chaque tours
txt = "votre nombre de point est de:"
scores = 10
print(txt, scores)
# scores = scores - 1
scores -= 1
print(txt, scores)
# scores = scores + 5
scores += 5
print(txt, scores)
# scores = scores / 2
scores /= 2
print(txt, scores)