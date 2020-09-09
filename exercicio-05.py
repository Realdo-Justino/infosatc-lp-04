extras01={
    "Vilão":"Dr.Robotnick",
    "Ano":2020
}
extras02={
    "Vilão":"Al",
    "Ano":2010
}
extras03={
    "Vilão":"Doofy Gilmore",
    "Ano":2020
}
filmes={
    "Sonic the Hedgehog":extras01,
    "Megamind":extras02,
    "Scary Movie":extras03
}
print("Listas de filmes com seus viloes e datas de lançamento: ")
for x in filmes:
    print(x,":",filmes[x])