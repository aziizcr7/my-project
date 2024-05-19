pcs = [('acer', 200), ('hp', 100), ('dell', 200.5)]


achats = {}


print("Bienvenue dans notre magasin d'informatique ! Voici les PC disponibles :")
for pc in pcs:
    print(f"- {pc[0]} : {pc[1]} €")


nom_pc_choisi = input("\nVeuillez choisir un PC par son nom : ").lower()


pc_trouve = False
for pc in pcs:
    if nom_pc_choisi == pc[0]:
        pc_trouve = True
        quantite = int(input(f"Combien de {nom_pc_choisi} souhaitez-vous acheter ? "))
        if quantite > 0:
            prix_total = pc[1] * quantite
            print(f"\nRécapitulatif de votre achat :")
            print(f"PC : {nom_pc_choisi}")
            print(f"Quantité : {quantite}")
            print(f"Total à payer : {prix_total} €")
            achats[nom_pc_choisi] = quantite
        else:
            print("La quantité doit être supérieure à zéro.")
        break

if not pc_trouve:
    print("Désolé, le PC choisi n'est pas disponible dans notre magasin.")
print("\nAchats enregistrés :")
for pc, quantite in achats.items():
    print(f"- {pc} : {quantite}")
