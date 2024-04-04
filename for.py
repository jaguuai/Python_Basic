sayilar=[1,3,5,7,9,12,19,21]

# 1-Sayilar listesindeki hangi sayılar 3 ün katidir?
for sayi in sayilar:
   if sayi%3==0:
     print(sayi)

      
# 2-Sayilar listesindeki sayıların toplamı kaçtır?
sum=0
for sayi in sayilar:
   sum+=sayi
   print(sum)
# 3-Sayilar listesindeki tek sayıların karesini alınız.
   

for sayi in sayilar:
   if(sayi%2==0):
    print(sayi**2)

sehirler=["kocaeli","istanbul","ankara","izmir","rize"]

# 4-Sehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
  if(len(sehir)<=5):
   print(f"{sehir} en fazla 5 karakterlidir")

urunler=[
  {"name":"samsung s6","price":"3000"},
  {"name":"samsung s7","price":"4000"},
  {"name":"samsung s8","price":"5000"},
  {"name":"samsung s9","price":"6000"},
  {"name":"samsung s10","price":"7000"}
]

# 5-Urunlerin fiyatları toplamı nedir?

sumPrice=0
for urun in urunler:
  sumPrice+=int(urun["price"])
print(sumPrice)
 
  
# 6-Urunlerin fiyatı en fazla 5000 olan ürünleri gösteriniz?

for urun in urunler:
  if(int(urun["price"])<=5000):
    print(urun["name"])