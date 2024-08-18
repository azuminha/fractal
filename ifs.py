from PIL import Image, ImageDraw
import math

# Image dimensions
width, height = 1024, 1024

# Create a new image with a white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

class Point:
    _t = 255
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
    def convert(self):
        new_x = 1024 * self.x
        new_y = 1024 - 1024 * self.y
        return (new_x, new_y)

class Polygon:
    def __init__(self, n: int):
        self.n = n
        self.lista: Point = []
        for i in range(n):
            self.lista.append(Point(0, 0))
    def set_point(self, x, y, i: int):
        self.lista[i].set(x, y)
    def get_polygon(self):
        n_list = []
        for i in range(self.n):
            n_list.append(self.lista[i].convert())
        return n_list
    def draw_polygon(self, draw):
        draw.polygon(self.get_polygon(), outline='black', fill='black')

class Triangle:
    def __init__(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(0, 0)
        self.p3 = Point(0, 0)
    def set_p1(self, p):
        self.p1 = p
    def set_p2(self, p):
        self.p2 = p
    def set_p3(self, p):
        self.p3 = p
    def get_triangle(self):
        return [self.p1.convert(), self.p2.convert(), self.p3.convert()]

def wi(p: Point, ei, fi) -> Point:
    x = 0.5 * p.x + ei
    y = 0.5 * p.y + fi
    return Point(x, y)

def w1(p: Point) -> Point:
    x = 0.5 * p.x + 0
    y = 0.5 * p.y + 0
    return Point(x, y)

def w2(p: Point) -> Point:
    x = 0.5 * p.x + 0.5
    y = 0.5 * p.y + 0
    return Point(x, y)

def w3(p: Point) -> Point:
    x = 0.5 * p.x + 0.25
    y = 0.5 * p.y + math.sqrt(3)/4
    return Point(x, y)

#p1 = Point(-0.5, 0)
#p2 = Point(0.5, 0)
#p3 = Point(0, math.sqrt(3)/2)
#t1 = Triangle()
#t2 = Triangle()
#t3 = Triangle()

wi = [w1, w2, w3]
tri = Polygon(4)
tri.set_point(0, 0, 0)
tri.set_point(1, 0, 1)
tri.set_point(0.5, math.sqrt(3)/2, 2)

def IFS(poly: Polygon, n: int = 1, i: int = 0):
    if n == i+1:
        poly.draw_polygon(draw)
        return 1
    # W(A) = A1 U A2 U A3
    for w in wi:
        tmp = Polygon(poly.n)
        for x in range(poly.n):
            pp = w(poly.lista[x])
            tmp.set_point(pp.x, pp.y, x)
        IFS(tmp, n, i+1)
    return 0     


IFS(tri, 8, 0)

#t1.set_p1(wi(p1, 0, 0))
#t1.set_p2(wi(p2, 0, 0))
#t1.set_p3(wi(p3, 0, 0))

#t2.set_p1(wi(p1, 0.5, 0))
#t2.set_p2(wi(p2, 0.5, 0))
#t2.set_p3(wi(p3, 0.5, 0))

#t3.set_p1(wi(p1, 0.25, math.sqrt(3)/4))
#t3.set_p2(wi(p2, 0.25, math.sqrt(3)/4))
#t3.set_p3(wi(p3, 0.25, math.sqrt(3)/4))

#draw.polygon(t1.get_triangle(), outline='black', fill='black')
#draw.polygon(t2.get_triangle(), outline='black', fill='black')
#draw.polygon(t3.get_triangle(), outline='black', fill='black')

# Save the image
image.save('IFS.png')