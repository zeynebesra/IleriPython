 # Class

class Employee():
    mesai = "9 - 18"
    sirket = "AS-AS"

    def __init__(self,isim,maas,yetenek,rutbe):  
        self.isim = isim
        self.yetenek = yetenek
        self.maas = maas
        self.gunsayisi = 0
        self.rutbe = rutbe,

    def calıs(self):                             
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1

    def terfi(self):                             
        print("Tebrikler ",self.isim,"Terfi aldın")
        self.maas+=200

    def bilgileriGoster(self):                   
        print("-"*40)
        print("Personelin ismi: ",self.isim)
        print("Personelin yetenekleri: ",self.yetenek)
        print("Personelin maaşı: ",self.maas)
        print("Personelin toplam gün sayısı",self.gunsayisi)
        print("Personelin konumu: ",self.rutbe)
        print("-"*40)

# staticmethod : hem sınıf adı üzerinden hem de örneklem adı üzerinden ulaşabileceğimiz bir metot yazsak 
# ve bu metodun sınıf içinde herhangi bir değişikliğe neden olmasını istemesek ama aynı zamanda sınıfa ait olmasını istersek
        @staticmethod 
        def prim_katsayisi():
            return 0.12


#  @classmethod : classmethod ise parametre olarak sınıfın kendisini alır.
#  Bu sayede sınıfla ilgili tüm bilgiye sahip olmaktadır. 
#  Eğer classmethod ile çalışıyorsanız sınıfın kendisi ya da nesne adı ile çağırılabilir.
       
       

#----------------------------------------------------------

Zey = Employee("Zeyneb",1600,"python,java,","Mühendis") 
Zey.calıs()
Zey.bilgileriGoster()