class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3,6)

print ("Rectangle 1: Area:", rectangle1.calculate_area(), "Perimeter:", rectangle1.calculate_perimeter())
print (rectangle2.calculate_perimeter())