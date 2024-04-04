list=["1","2","5a","10b","abc"]

#1:Liste elemanları içindeki sayısal değerleri bulunuz.
for i in list:
    try:
      result= int(i)
      print(result)
    except ValueError:
       continue
# 2:Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı oldundan emın olunuz ,aksı halde hata mesajı
while True:
    sayi=input("sayi")
    if sayi == "q":
     break
    try:
      result=float(sayi)
      print("girdiğiniz sayi:",result)
    except ValueError:
     print("gecersız sayı")
     continue
      
# 3:Girilen parola içinde türkçe karakter hatası verınız
# turkısh_characters="şçqüöıi"
# password=input("parola giriniz: ")
# for i in password:
#   if i in turkısh_characters:
#    raise TypeError("Parola Turkce Karakter Iceremez.")
#   else:
#     pass
  
# print("Gecerli parola")
    
def chech_password():
   turkısh_characters="şçqüöıi"
   for i in password:
     if i in turkısh_characters:
       raise TypeError("Parola Turkce Karakter Iceremez.")
     else:
       pass
   print("Gecerli parola") 

password=input("parola giriniz: ")

try:
   chech_password(password)
except TypeError as err:
   print(err)

# 4:Faktöryel fonk olustur ve fonk a gelen degerler ıcın hata mesajları uret


def factorial(x):
    x=int(x)

    if x<0:
        raise ValueError("Negatif deger")
    
    result=1

    for i in range(1,x+1):
       result *=i
    return result   

for x in [5,10,20,-3,"10a"]:
   try: 
        y=factorial(x)
   except TypeError as err:
        print(err) 
        continue
print(y)