import math

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Line:
    def __init__(self, point1, point2):
         self.point1 = point1
         self.point2 = point2
         self.length = math.hypot(self.point2.x - self.point1.x, self.point2.y - self.point1.y)

class Triangle:
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        s = (line1.length + line2.length + line3.length) / 2
        s1 = s - line1.length
        s2 = s - line2.length
        s3 = s - line2.length
        self.area = math.sqrt(s * (s1) * (s2) * (s3))

iterations = int(input())

answers = []

for i in range(iterations):
    x1,y1,x2,y2,x3,y3 = input().split()

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    point3 = Point(x3, y3)
    
    l1 = Line(point1, point2)
    l2 = Line(point1, point3)
    l3 = Line(point2, point3)
    
    triangle = Triangle(l1, l2, l3)
    
    answers.append(str(triangle.area))

print(' '.join(answers))