x,y,z=2,5,10
numbers= 1,5,7,10,6

# 1-Kullanıcıdan aldıgınız 2 sayının carpımı ile x,y,z toplamının farkı nedir?
userA=int(input("1. sayi: "))
userB=int(input("2. sayi: "))
userAB=userA*userB
sumxyz=x+y+z

result=userAB-sumxyz
print(result)

# 2- y nin x e kalansız bölümünü hesaplayınız.
z=y//x
print(z)
# 3- (x,y,z) toplamının mod 3 ü nedir?
mod3=sumxyz%3
print(mod3)
# 4- y nin x. kuvvetini hesaplayınız.
result=y**x
print(result)
# 5- x ,*y,z= numbers işlemine göre z nin küpü kaçtır?

x ,*y,z= numbers
result=z**3
print(result)
# 6- x,*y,z=numbers işlemine göre y nin değerleri toplamı kaçtır?

result=y[0]+y[1]+y[2]
print(result)
