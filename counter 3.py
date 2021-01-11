stringa = input("Scrivi una parola --> ")
lista_lettere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
stringa = list(stringa.upper())
for lettera in lista_lettere:
    if stringa.count(lettera) > 0:
        print(lettera, " : " ,stringa.count(lettera))
