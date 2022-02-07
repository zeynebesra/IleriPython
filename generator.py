# Generatör : Generatörler de iteratörler gibi __next__() fonksiyonuna sahiptir 
# ve bu sayede iterasyon işlemine tabi tutulabilirler. 
# Generatörlerde elinizde iterasyona tabi tutacağınız elemanlar halihazırda mevcut değildir, 
# siz bir sonrakini çağırdığınız zaman üretilir ve size sunulur. 
# !! return ifadesi bir fonksiyonu sonlandırırken, 
#  yield ifadesi değeri döndürür, saklar ve fonksiyonu çağırma devam eder.
def my_gen():
    i = 1
    print('Birinci :')
    yield i
 
    i += 1
    print('İkinci :')
    yield i
 
    i += 1
    print('Üçüncü :')
    yield i
 
a = my_gen()

print(next(a))
print(next(a))
print(next(a))
