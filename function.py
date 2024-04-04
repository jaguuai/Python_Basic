#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonsiyon yazınız

def printWord(word,amount):
    print(word*amount)

printWord("jagu\n",5)

#2- Kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye cevirene fonksiyon

def toList(*params):
    list=[]

    for param in params:
        list.append(param)
    
    return list

result=toList(10,20,30,"jagu")
print(result)

#3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

def Primary(a,b):
    for sayi in range(a,b+1):
        if(sayi>1):
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
                else:
                    print(sayi)

a=int(input("1.sayi:"))
b=int(input("2. sayi:"))

Primary(a,b)

#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde geri gönderen fonksiyon

def divisor(sayi):
    divisors=[]

    for i in range(2,sayi):
        if(sayi % i==0):
            divisors.append(i)
    return divisors

print(divisor(20))
         


    