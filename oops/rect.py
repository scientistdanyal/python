class Rectangle():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def get_area(self):
        area = self.height * self.width
        print(f'Area: {area}')
    

    def get_perimeter(self):
        permiter = 2 * (self.height + self.width)
        print(f'Perimeter: {permiter}')
      
    
                      

rect = Rectangle(4,5)

rect.get_area()
rect.get_perimeter()
