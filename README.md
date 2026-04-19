# veri yapıları ödevi - arama ve sıralama algoritmaları

bu ödevde arama ve sıralama algoritmalarını python ile yazdım. toplamda 2 arama 5 sıralama algoritması var.

---

## dosyalar

- `algorithms.py` → bütün algoritmalar burada, en altta da test kodu var

---

## nasıl çalıştırılır

python 3 yüklüyse direkt çalışır, başka bir şey gerekmiyor.

```
python algorithms.py
```

---

## arama algoritmaları

### linear search

listenin en başından başlayıp her elemana tek tek bakıyor. aradığımız sayıya ulaşınca o elemanın index numarasını döndürüyor, bulamazsa -1 döndürüyor.

basit ama liste büyüdükçe yavaşlıyor çünkü en kötü ihtimalle tüm listeye bakmak zorunda kalıyor.

- zaman karmaşıklığı: **O(n)**

### binary search

bu algoritma sadece **sıralı listelerde** çalışıyor. önce ortadaki elemana bakıyor, aradığımız sayı ondan küçükse sol yarıya geçiyor, büyükse sağ yarıya. böyle daraltarak buluyor.

linear search'e göre çok daha hızlı ama listeyi önce sıralamak gerekiyor.

- zaman karmaşıklığı: **O(log n)**

---

## sıralama algoritmaları

### bubble sort

yan yana iki elemanı karşılaştırıyor, soldaki sağdakinden büyükse yer değiştiriyor. bunu sürekli tekrar edince büyük elemanlar yavaş yavaş sona doğru kayıyor. adını da buradan alıyor sanırım.

anlaması kolay ama büyük listelerde yavaş.

- zaman karmaşıklığı: **O(n²)**

### selection sort

her adımda sıralanmamış kısımdaki en küçük elemanı buluyor ve o adımın başına koyuyor. bubble sort'a benziyor ama daha az yer değiştirme yapıyor.

- zaman karmaşıklığı: **O(n²)**

### insertion sort

elimizdeki iskambil kartlarını sıralamak gibi düşünebiliriz. her elemanı alıp sol taraftaki sıralı kısımda doğru yerine sokuyor. neredeyse sıralı listelerde gayet hızlı çalışıyor.

- zaman karmaşıklığı: **O(n²)**, neredeyse sıralı listede **O(n)**

### merge sort

listeyi ortadan ikiye böler, her iki parçayı kendi içinde sıralar (bunu da yine aynı fonksiyonu çağırarak yapıyor), sonunda iki sıralı parçayı birleştirir. büyük listelerde iyi çalışıyor ama ekstra bellek kullanıyor.

- zaman karmaşıklığı: **O(n log n)**

### quick sort

listeden bir pivot eleman seçiyor (ben ortadakini seçtim). pivottan küçük olanları sola, büyük olanları sağa ayırıyor. sonra sol ve sağ tarafı da aynı şekilde sıralıyor. ortalamada hızlı ama kötü pivot seçilince yavaşlayabiliyor.

- zaman karmaşıklığı: ortalama **O(n log n)**, en kötü **O(n²)**

---

## karşılaştırma tablosu

| algoritma | en iyi | ortalama | en kötü | ekstra bellek |
|---|---|---|---|---|
| linear search | O(1) | O(n) | O(n) | yok |
| binary search | O(1) | O(log n) | O(log n) | yok |
| bubble sort | O(n) | O(n²) | O(n²) | yok |
| selection sort | O(n²) | O(n²) | O(n²) | yok |
| insertion sort | O(n) | O(n²) | O(n²) | yok |
| merge sort | O(n log n) | O(n log n) | O(n log n) | var |
| quick sort | O(n log n) | O(n log n) | O(n²) | yok |

---

## genel yorum

küçük listeler için hangisini kullanırsanız kullanın pek fark etmiyor. ama liste büyüdükçe bubble/selection/insertion sort gerçekten çok yavaşlıyor. o yüzden büyük verilerde merge sort ya da quick sort tercih etmek daha mantıklı.

binary search linear search'e göre çok daha hızlı ama kullanmadan önce listeyi sıralamayı unutmamak lazım.
