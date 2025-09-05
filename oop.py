class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
t1 = Triangle(9, 20, 18)
perimeter1 = t1.perimeter()

t2 = Triangle(7, 4, 9)
perimeter2 = t2.perimeter()

print("Perimeter: ", perimeter1)
print("Perimeter: ", perimeter2)