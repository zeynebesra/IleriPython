#closure : dışdaki fonk çağrıldığında bile içteki fonksiyon dıştaki fonk variable erişim sağlayabilme.

# example 1
def outer():
    msg = "Hey"

    def inner():
        print(msg)
        
    return inner()

f = outer()
f

#example 2
def outer(name):
    # this is the enclosing function

    def inner():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'name'
        print(name)

    return inner

# call the enclosing function
myFunction = outer('Zey')
myFunction()