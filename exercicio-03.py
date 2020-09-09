dicionario={
    "pessoa":"Boa",
    "id":218,
    "nome":"Realdo",
    "cpf":12143,
    "telefone":67325325,
    "email":"naoemeuemail@gmail.com"
}
print("Os valores do dicionario são: ")
for x in dicionario.values():
    print(x)

dicionario["endereço"]="Rodeio da Areia"
dicionario["sexo"]="m"

print(" ")
print("O dicionario é")
for x in dicionario:
    print(x,":",dicionario[x])