"""
Soru:Girilen bir sayının asal olup olmadığını bulun.
**Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
"""

number=int(input("Sayi giriniz: "))
isPrime=True

if number==1:
    isPrime=False
for i in range(2,number):
    if(number %i == 0):
     isPrime=False
     break

if isPrime:
   print("Girdiğiniz sayi asaldır")
else:
   print("Sayi asal değildir.")
