class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        width = self.width
        height = self.height
        if width > 50 or height > 50:
            return "Too big for picture."
        pic = ""
        column = ""
        for i in range(width):
            column += "*"
        for j in range(height):
            pic += column + "\n"
            # if j != max(0,height - 1):
            #     pic += "\n"
        return pic
    
    def get_amount_inside(self, shape):
        area1 = self.get_area()
        area2 = shape.get_area()
        return int(area1 / area2)
    
    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
 

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __repr__(self):
        return "Square(side=" + str(self.width) + ")"

#%% test
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))