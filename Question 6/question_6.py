# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:45:15 2021

@author: ravichandrapl
"""
from shapely.geometry import Point, Polygon

# Create a Polygon
coords = [(1,1), (1,5),(10,1), (10,5)]
poly = Polygon(coords)

points = input("Enter the points with space between the x and y coordinate: ").split()
if len(points) != 2:
    break
point = Point (float(points[0]), float(points[1]))
if point.within(poly):
    print("Inside")
else:
    print("Outside")
