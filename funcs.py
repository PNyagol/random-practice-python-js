def greet():
    print('Hello')
greet()


def calculate(x, y):
    mult = x*y
    sub = x - y
    sum = x + y
    return sum, mult, sub
print(calculate(8, 3))
print(calculate(20, 32))
print(calculate(238, 13))


def salamu(greeting):
    print(greeting)
salamu("Ber Nyagol")
salamu("in nade?")


def mos(ber = "How are you nyagol"):
    print(ber)
mos()
mos("Amosi ni ber nyakwar Mama?")