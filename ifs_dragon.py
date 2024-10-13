from PIL import Image, ImageDraw
import math

# Image dimensions
width, height = 4096, 4096

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
        #new_x = 1024 * self.x
        #new_y = 1024 - 1024 * self.y
        #new_x = 512*(self.x + 1)
        #new_y = 1024 - 512*(self.y + 1)
        new_x = 4096/2*(self.x + 1)
        new_y = 4096 - 4096/2*(self.y + 1)
        return (new_x, new_y)
    def print(self):
        print(f"x: {self.x}, y: {self.y}")

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
    def print(self):
        print("Poly: ")
        for i in range(self.n):
            self.lista[i].print()

def w1(p: Point) -> Point:
    angle = math.pi/4
    x = (1/math.sqrt(2)) * (p.x * math.cos(angle) - p.y * math.sin(angle)) + 0
    y = (1/math.sqrt(2)) * (p.x * math.sin(angle) + p.y * math.cos(angle)) + 0
    return Point(x, y)

def w2(p: Point) -> Point:
    angle = 135 * math.pi / 180
    x = (1/math.sqrt(2)) * (p.x * math.cos(angle) - p.y * math.sin(angle)) + 1
    y = (1/math.sqrt(2)) * (p.x * math.sin(angle) + p.y * math.cos(angle)) + 0
    return Point(x, y)

wi = [w1, w2]
line = Polygon(2)
line.set_point(0, 0, 0)
line.set_point(1, 0, 1)

def IFS(poly: Polygon, n: int = 1, i: int = 0):
    if n == i+1:
        poly.draw_polygon(draw)
        #poly.print()
        return 1
    # W(A) = A1 U A2 U A3
    for w in wi:
        tmp = Polygon(poly.n)
        for x in range(poly.n):
            #print(x)
            pp = w(poly.lista[x])
            tmp.set_point(pp.x, pp.y, x)
        IFS(tmp, n, i+1)
    return 0     


#IFS(tri, 8, 0)
IFS(line, 18, 0)

# Save the image
image.save('IFS.png')