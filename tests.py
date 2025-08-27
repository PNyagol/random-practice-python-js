def greet(name, food):
    print(f"Hello, {name}!. How is the {food}")

greet("Peter Nyagl", "fish")
greet("Joan Winga", "rice")

# name and foo are paramenters [variables in function definitions]
# Peter Nyagol, fish are arguments [actual values for the variables]
# like in this: x = 2 [x is a variabe - parameter and 2 is its value - argument]

# Return Statement

def mult(a, b):
    return a * b
results = mult(8, 4)
result2 = mult(4, 4)

print(result2)
print(mult(45, 4))
print(results)