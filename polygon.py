#!/usr/bin/python
import math
class Point:
	x = 0
	y = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def asTuple(self):
		return (self.x , self.y)
		
class Line:
	endPoints = []
	
	
	def __init__(self,end1,end2):
		self.endPoints.append(end1)
		self.endPoints.append(end2)
		
	def getLength(self):
		x1,y1 = self.endPoints[0].asTuple()
		x2,y2 = self.endPoints[1].asTuple()
		length = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		return length
	
	
	
			
		
class Triangle:
	points = []
	sideLengths = []
	def __init__(self,points):
		self.points = points
		self.makeSideLengths()
	def makeSideLengths(self):
		self.sideLengths.append(Line(self.points[0],self.points[1]).getLength())
		self.sideLengths.append(Line(self.points[2],self.points[1]).getLength())
		self.sideLengths.append(Line(self.points[2],self.points[0]).getLength())
	def area(self):
		p = 0
		for length in self.sideLengths:
			p += length
		p = p/2
		a = math.sqrt(p*(p-self.sideLengths[0])*(p-self.sideLengths[1])*(p-self.sideLengths[2]))
		return a
		
class Polygon:
	points = []
	triangles = []
	def __init__(self,points):
		
		self.points = points
		
	def drawTriangles(self):
		numOfPoints = len(self.points)
		x = 1
		y = 2
		while y < numOfPoints:
			source = self.points[0]
			p1 = self.points[x]
			p2 = self.points[y]
			x += 1
			y += 1
			newTriangle = Triangle([source,p1,p2])
			self.triangles.append(newTriangle)
			
			
	def area(self):
		self.drawTriangles()
		area = 0
		for triangle in self.triangles:
			print triangle.area()
			area += triangle.area()
		return area
		
def main():
	inp = open("input","r")
	sideNum = int(inp.readline())
	points = []
	for x in range(sideNum):
		x,y = map(float,inp.readline().split())
		
		points.append(Point(x,y))
	poly = Polygon(points)
	print(poly.area())
	
main()
