# arama algoritmalari odevi

# --------------------------------
# linear search
# --------------------------------
# listeyi bastan sona gez, bulunca indexi dondur
def linear_search(liste, sayi):
    for i in range(len(liste)):
        if liste[i] == sayi:
            return i
    return -1   # bulamazsa -1


# --------------------------------
# binary search
# --------------------------------
# ortaya bak, kucukse sola git, buyukse saga git
# dikkat: liste sirali olmali yoksa calismiyor
def binary_search(liste, sayi):
    sol = 0
    sag = len(liste) - 1

    while sol <= sag:
        orta = (sol + sag) // 2
        if liste[orta] == sayi:
            return orta
        elif liste[orta] < sayi:
            sol = orta + 1
        else:
            sag = orta - 1

    return -1


# --------------------------------
# test
# --------------------------------
liste = [38, 27, 43, 3, 9, 82, 10]
sirali_liste = sorted(liste)
aranan = 43

print("liste:", liste)
print("sirali liste:", sirali_liste)
print("aranan sayi:", aranan)
print()

sonuc = linear_search(liste, aranan)
print("linear search ->", aranan, "sayisi", sonuc, ". indexte bulundu")

sonuc2 = binary_search(sirali_liste, aranan)
print("binary search ->", aranan, "sayisi", sonuc2, ". indexte bulundu (sirali listede)")
