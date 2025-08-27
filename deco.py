def greets(name):
    return f"Hello, {name}"

say_hello = greets
print(say_hello('Peter Nyagol'))

# A decorator is a function that takes another function as input and returns a new function.

def my_decorator (func):
    def wrapper():
        print("Before the func runs")
        func()
        print("After the func runs")
    return wrapper

@my_decorator
def say_hi():
    print("hi")

say_hi()

# The @my_decorator syntax is shorthand for: say_hi = my_decorator(say_hi)