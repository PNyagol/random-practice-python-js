class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c

#..........User Inputs............#

a = int(input("Enter Side a: "))
b = int(input("Enter Side b: "))
c = int(input("Enter Side c: "))

#......Using Inputs to Create Object.....#
t = Triangle(a, b, c)
perimeter1 = t.perimeter()
print(f"Perimeter of the Triangle is: {perimeter1}")
