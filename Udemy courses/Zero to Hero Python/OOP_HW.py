from cmath import pi


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        d = ((x2 - x1 )**2 + (y2 - y1)**2)**0.5
        return d
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        m = (y2-y1)/(x2 - x1)
        return m




coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        r , h = self.radius, self.height
        V = pi*(r**2)*h
        return round(V, 2)
    
    def surface_area(self):
        r , h = self.radius, self.height
        A = 2 * pi * r * h + 2 * pi * (r**2)
        return round(A, 2)




c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())