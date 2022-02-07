#decorator:
# Bir dekoratör kullanıldığında, kullanılan fonksiyon dekoratöre parametre olarak düşer. 
# Dekoratör içinde bir kapsayıcı (wrapper) iç fonksiyon oluşturur ve asıl fonksiyona gelen parametreleri bununla yakalarız.
#  Dilediğimiz işlemleri yaptıktan sonra iç fonksiyondan, parametre olarak gelen asıl fonksiyondan dönen değeri, 
#  dekoratörden ise iç fonksiyonun kendisini geriye döndürürüz.

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Fonksiyon çalışacak...')
        func()
    return wrapper


@decorator
def func():
    print('Fonksiyon çalıştı.')


func()