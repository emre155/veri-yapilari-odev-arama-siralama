# arama ve siralama algoritmalari odevi

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
# bubble sort
# --------------------------------
# yanindakinden buyukse yer degistir, boyle boyle buyukler sona gider
def bubble_sort(liste):
    arr = liste[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --------------------------------
# selection sort
# --------------------------------
# her seferinde en kucugu bul, one al
def selection_sort(liste):
    arr = liste[:]
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


# --------------------------------
# insertion sort
# --------------------------------
# iskambil kagidi gibi, her elemani dogru yerine sok
def insertion_sort(liste):
    arr = liste[:]
    for i in range(1, len(arr)):
        el = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = el
    return arr


# --------------------------------
# merge sort
# --------------------------------
# ikiye bol, her parcayi ayri sirala, sonra birlestir
def merge_sort(liste):
    if len(liste) <= 1:
        return liste

    orta = len(liste) // 2
    sol = merge_sort(liste[:orta])
    sag = merge_sort(liste[orta:])

    # birlestirme kismi
    sonuc = []
    i = 0
    j = 0
    while i < len(sol) and j < len(sag):
        if sol[i] <= sag[j]:
            sonuc.append(sol[i])
            i += 1
        else:
            sonuc.append(sag[j])
            j += 1

    # kalan elemanlari ekle
    while i < len(sol):
        sonuc.append(sol[i])
        i += 1
    while j < len(sag):
        sonuc.append(sag[j])
        j += 1

    return sonuc


# --------------------------------
# quick sort
# --------------------------------
# ortadaki elemani pivot sec, kucukleri sola buyukleri saga at
def quick_sort(liste):
    if len(liste) <= 1:
        return liste

    pivot = liste[len(liste) // 2]
    sol = []
    orta = []
    sag = []

    for x in liste:
        if x < pivot:
            sol.append(x)
        elif x == pivot:
            orta.append(x)
        else:
            sag.append(x)

    return quick_sort(sol) + orta + quick_sort(sag)


# --------------------------------
# test
# --------------------------------
liste = [38, 27, 43, 3, 9, 82, 10]
sirali_liste = sorted(liste)
aranan = 43

print("liste:", liste)
print("sirali liste:", sirali_liste)
print()

print("=== arama ===")
sonuc = linear_search(liste, aranan)
print("linear search,", aranan, "sayisi ->", sonuc, ". indexte bulundu")

sonuc2 = binary_search(sirali_liste, aranan)
print("binary search,", aranan, "sayisi ->", sonuc2, ". indexte bulundu (sirali listede)")

print()
print("=== siralama ===")
print("bubble sort    :", bubble_sort(liste))
print("selection sort :", selection_sort(liste))
print("insertion sort :", insertion_sort(liste))
print("merge sort     :", merge_sort(liste))
print("quick sort     :", quick_sort(liste))
