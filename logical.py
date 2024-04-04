#1-Girilen bir sayının 0-100 arasında olup olmadıgını kntrol edınız.
sayi=int(input("Sayi giriniz: "))
result=sayi>0 and sayi<100
print(result)
#2-Girilen bir sayının poizitif sayı olup olmadıgını kontrol ediniz.
result=sayi>0
print(result)
#3-Email ve parola bilgileri ile giriş kontrolü yapınız.
email="ayse@gmail.com"
password="123"

isUser=input("Mail giriniz: ")==email and input("Sifre giriniz: ")==password
print(isUser)
#4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1=input("1. sayıyı giriniz: ")
sayi2=input("2. sayıyı giriniz: ")
sayi3=input("3. sayıyı giriniz: ")

result=sayi1>sayi2 and sayi1>sayi3
print(f"sayi1 en büyük sayidir: {result}")
result=sayi2>sayi1 and sayi2>sayi3
print(f"sayi2 en büyük sayidir: {result}")
result=sayi3>sayi2 and sayi3>sayi1
print(f"sayi3 en büyük sayidir: {result}")


#5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#      Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#      a)Ortalama 50 olsa bile final notu en az 50 olmalıdır
#      b)Finalden 70 alındığında ortalamanın önemi olmasın.
vize1=int(input("Vize1: "))
vize2=int(input("Vize2: "))
final=int(input("Final: "))
ortalama= ((vize1+vize2/2)*0.6)+(final*0.4)
result=(ortalama>=50 and final>=50) or (final>=70)
print(f'Ogrencinin ortalaması:{ortalama}ve geçme durumu:{result}')
#6-Kişinin adı,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#      Formül:(Kilo/boy uzunluğunun karesi)
#      Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#      0-18.4 => Zayıf
#      18.5-24.9 => Normal
#      25.0-29.9 => Fazla Kilolu
#      30.0-34.9 => Şişman(Obez)

name=input("adiniz: ")
kg=float(input("kilonuz: "))
hg=int(input("boyunuz: "))

index=kg/(hg**2)
zayif=(index>=0)and (index<=18.4)
normal=(index>18.4)and (index<=24.9)
kilolu=(index>24.9)and (index<=29.9)
obez=(index>=29.9)and (index<=34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")