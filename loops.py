'''

1-100 arasında rastgele üretilecek bir sayıyı asagı yukarı ifadeleri ile buldurmaya 
çalışın. (hak=5)
** "random modulu" icin "ptyhon random" seklınde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
**Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random
randomNumber=random.randint(1,100)
rights=5
counter=0

while rights>0:
  rights-=1
  counter+=1
  userNumber=int(input("1 ile 100 arasında bir sayı giriniz:")) 
  if(randomNumber==userNumber):
   print(f"tebrikler {counter}. tahminde bildiniz.Toplam puanınız:{100-(20)*(counter-1)}")
   break
  elif randomNumber>userNumber:
    print("yukari")
  else:
    print("asagi")  
  if rights==0:
    print(f"hakkiniz bitti Tutulan sayi:{randomNumber}")

   

  
