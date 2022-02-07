 # Inheritance (Miras/Kalıtım)

class Kullanici:
    def __init__(self,adi,soyadi,numara):
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara
 
 
    def giris(self):
        print("Giriş Yapıldı")
 
    def cikis(self):
        print("Çıkış yapıldı")
 
 
 
class Akademisyen(Kullanici):
    pass
class Personel(Kullanici):
    pass
class Ogrenci(Kullanici):
    pass

# Kullanıcı isimli sınıfımızı oluşturduk ve diğer nesneleri bu sınıftan miras aldık.
# Alt sınıflar için özellik ve işlev eklemedik çünkü biz özellik ve işlevleri 
# kullanıcı sınıfından miras alıyoruz.

akademisyen = Akademisyen("Zeyneb","Öztürk",1236521)
personel = Personel("Esra","Öztürk",1539527)
ogrenci = Ogrenci("Eda","Öztürk",1436589)
print("-"*30)
print("Akademisyen")
print("-"*30)
print(akademisyen.adi)
print(akademisyen.soyadi)
print(akademisyen.numara)

print("-"*30)
print("Personel")
print("-"*30)
print(personel.adi)
print(personel.soyadi)
print(personel.numara)

print("-"*30)
print("Öğrenci")
print("-"*30)
print(ogrenci.adi)
print(ogrenci.soyadi)
print(ogrenci.numara)

