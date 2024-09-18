import builtins


x='global x'

def test_global():
    
    global X
    x ='global x changed' # it will change the value of x even for global changes
    y='local y'
    print(y)
    print(x)

test_global()

print(x)

m= min([1,2,3,4])
print(m)


def outer():
    
    a='outer a'
    print(a)
    
    def inner():
        # nonlocal b  variables to make it accessible outside of the function
        b='inner b'
        print(a)
        print(b)
    
    inner()
outer()
