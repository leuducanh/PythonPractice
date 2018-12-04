
def make(f):
    print("abc")
    f()


def ordinary():
    print("I am ordinary")

def divide(a,b):
    return a/b

print("a")
ordinary  = make(ordinary)
print("a")