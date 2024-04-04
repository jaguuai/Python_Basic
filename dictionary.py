ogrenciler={}

number=input("student no:" )
name=input("student name:" )
surname=input("student surname:" )
phone=input("student tel-no:" )

# ogrenciler[number]={
#     'name':name,
#     'surname':surname,
#     'tel':phone
# } asagıdakı kod ile aynı çalışır farkı asagıdakı kod bırden fazla aynı anda eklemeye ızın verır

ogrenciler.update({
    number:{
         'name':name,
    'surname':surname,
    'tel':phone
    },
     number:{
         'name':name,
    'surname':surname,
    'tel':phone
    }
})

print(ogrenciler)

ogrNo=input("student no:")
ogrenci=ogrenciler[ogrNo]
print(ogrenci)


