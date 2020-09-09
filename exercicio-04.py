listaSegunda=["Sociologia","Historia","Fisica"]
listaTerca=["Literatura","Biologia"]
listaQuarta=["Matematica","Produção de Textos","Educaçõa Fisica"]
listaQuinta=["Ingles","Lingua Portuguesa"]
listaSexta=["Quimica","Geografia"]

dicionario={
    "Segunda":listaSegunda,
    "Terça":listaTerca,
    "Quarta":listaQuarta,
    "Quinta":listaQuinta,
    "Sexta":listaSexta
}
print("O dicionario é")
for x in dicionario:
    print(x,":",dicionario[x])