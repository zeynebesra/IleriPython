# ------------------------------------------------------------------------------------------------
#(*args): Aslında *rakamlar ile arasında hiçbir fark yoktur. 
#  Asıl önemli önemli nokta, parametreden önce kullandığımız yıldız (*) yapısıdır.
#  Python kullanıcıları için *args geleneksel bir parametredir.
#  Bu geleneksel parametre Python kodumuzun kullanıcılar tarafından
#  hem daha rahat anlaşılabilmesi için hem de okunabilirliğini arttırabilmek için önemlidir. 

def fonksiyon(*args):
 
    for i in args:
        print(i)
 
liste = [10, 2.5, 'zey', True]
 
fonksiyon(liste)
 
#sonuç
#[10, 2.5, 'burak', True]

# ----------------------------------------------------------------------------------------------------
# (**kwargs) :Çift yıldızlı (**) parametrelerin tek yıldızlı (*) 
# parametrelerden en önemli farkı, fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabilmemizdir.
# Burada, fonksiyon parametresinden önce çift yıldız(**)
# kullandığımız için sonucumuz sözlük (dictionary) olarak döner.


def fonksiyon1(**parametre):
    print(parametre)
 
fonksiyon1(deger1='Zey', deger2=20)
fonksiyon1(deger1='Zey', deger2=20, deger3=True, deger4=15.2)

# beraber kullanımı

def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print('anahtar: ',k,'Degerimiz: ',v)
 
fonksiyon(1,2,3,'args' , deger = 'kwargs')