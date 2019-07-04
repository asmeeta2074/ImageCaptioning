class Pyramid:
    def get_vol(length,height):
        return (length**2 * height)/3
    def get_area(length,height):
        slant_height = ((length/2)**2+height**2)**0.5
        return (length*slant_height)/2
    
p = Pyramid
print(p.get_vol(1,3))
print(p.get_area(8,3))