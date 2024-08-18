from PIL import Image, ImageDraw
import math
import random

# Image dimensions
width, height = 1024, 1024

# Create a new image with a white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

sierpinski = 1

class Point:
    _t = 255
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
    def convert(self):
        if sierpinski == 1:
            new_x = 1024 * self.x
            new_y = 1024 - 1024 * self.y
        else:
            new_x = 1024*(self.x + 3)/6
            new_y = 1024 - 1024*self.y/10
        return (new_x, new_y)
    def draw(self, draw):
        point_radius = 1
        tmp = self.convert()
        x = tmp[0]
        y = tmp[1]
        draw.ellipse((x - point_radius, y - point_radius, x + point_radius, y + point_radius), fill='black')

def f1(p: Point) -> Point:
    x = 0 * p.x + 0 * p.y + 0
    y = 0 * p.x + 0.16 * p.y + 0
    return Point(x, y)

def f2(p: Point) -> Point:
    x = 0.85 * p.x + 0.04 * p.y + 0
    y = -0.04 * p.x + 0.85 * p.y + 1.60
    return Point(x, y)

def f3(p: Point) -> Point:
    x = 0.20 * p.x - 0.26 * p.y + 0
    y = 0.23 * p.x + 0.22 * p.y + 1.60
    return Point(x, y)

def f4(p: Point) -> Point:
    x = - 0.15 * p.x + 0.28 * p.y + 0
    y = 0.26 * p.x + 0.24 * p.y + 0.44
    return Point(x, y)


barnsley_prob = [0.01, 0.85, 0.07, 0.07]
barnsley = [f1, f2, f3, f4]

prob = [1/3, 1/3, 1/3]
tri  = [Point(0, 0),
        Point(1, 0),
        Point(1/2, math.sqrt(3)/2)]

gen_points = 300000
r = 1/2
start_point = Point(0, 0)
for _ in range(gen_points):
    if sierpinski == 1:
        get_point = random.choices(tri, weights=prob)[0]
        new_point = Point(start_point.x  + (get_point.x - start_point.x)*r, start_point.y  + (get_point.y - start_point.y)*r)
    else:
        fi = random.choices(barnsley, weights=barnsley_prob)[0]
        get_point = fi(start_point)
        new_point = get_point
    new_point.draw(draw)
    start_point = new_point

image.save('IFS_CHAOS.png')