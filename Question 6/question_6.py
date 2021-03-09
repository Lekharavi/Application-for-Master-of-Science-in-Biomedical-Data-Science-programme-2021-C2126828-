# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:45:15 2021

@author: ravichandrapl
"""
from shapely.geometry import Point, Polygon

# Create Point objects
p1 = Point(1,1)
p2 = Point(1,5)

# Create a Polygon
coords = [(1,1), (1,5),(10,1), (10,5)]
poly = Polygon(coords)

#input the pompting questions
