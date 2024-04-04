sayilar=[1,3,5,7,9,12,19,21]

#1-Sayilar listesini while ile ekrana yazdıralım
x=0
while x<len(sayilar):
    print(sayilar[x])
    x+=1
#2-Başlangic ve bitis degerlerini kullanıcıdan alıp aradaki tüm tek sayilari ekrana yazdıralım
    startValue=int(input("Start Value: "))
    endValue=int(input("End Value: "))
    
    x=startValue
    while x<endValue:
        if(x%2==1):
         print(x)
        x+=1

#3-1-100 arasındaki sayıları azalan sekılde yazdırın
a=100
while a>0:
   print(a)
   a-=1
    
#4-Kullancıdan alacagınız 5 sayıyı ekranda sıralı bır sekılde yazdırın
numbers=[]
i=0
while i<5:
   sayi=int(input("sayi: "))
   numbers.append(sayi)
   i+=1
numbers.sort()   
print(numbers)

#5-Kullancıdan alacagınız sınırsız urun bılgısını urunler listesi içinde saklanıyor
#      -ürün sayısını kullanıcıya sorun
#      -dictinonary listesi yapısı (name,price) seklinde olsun
#      -ürün ekleme işlemi bittiğinde ürünler, ekranda while ile listeleyin

urunler=[]

urunSayisi=int(input("Urun sayisi: "))
i=0
while i<urunSayisi:
     name=input("urun ismi: ")
     price=input("urun fiyatı: ")
     urunler.append({
     "name":name,
     "price":price
     })
     i+=1
for urun in urunler:
   print(f"ürün adı: {urun[name]} ürün fiyatı:{urun[price]}")    