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
        new_x = 4096/10*(self.x + 5)
        new_y = -4096/10*(self.y - 5)
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

a = math.pi/4
cos = math.cos
sin = math.sin
def w1(p: Point) -> Point:
    x = p.x * (cos(a) * cos(a)) + p.y * (-cos(a) * sin(a)) + 0
    y = p.x * (cos(a) * sin(a)) + p.y * (cos(a) * cos(a)) + 1
    return Point(x, y)

def w2(p: Point) -> Point:
    x = p.x * (sin(a) * sin(a)) + p.y * (cos(a) * sin(a)) + (cos(a) * cos(a))
    y = p.x * (-cos(a) * sin(a))+ p.y * (sin(a) * sin(a)) + 1 + (cos(a) * sin(a))
    return Point(x, y)

def w3(p: Point) -> Point:
    return Point(p.x, p.y)

wi = [w1, w2, w3]
line = Polygon(4)
line.set_point(0, 0, 0)
line.set_point(0, 1, 1)
line.set_point(1, 1, 2)
line.set_point(1, 0, 3)


ans = 0
def IFS(poly: Polygon, n: int = 1, i: int = 0):
    global ans
    if n == i+1:
        poly.draw_polygon(draw)
        ans += 1
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
IFS(line, 13, 0)
print(ans)
# Save the image
image.save('IFS.png')