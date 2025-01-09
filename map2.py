import pygame
import math

from map1 import ellipse_points_x, ellipse_points_y


inner_points, outer_points, obstacle_points= [],[],[]
track_width=5000
track_height=4000


#end of straight
for y in range(840, 590, -10):
    outer_points.append((280, y))
    inner_points.append((520,y))

#curve 1 outer h
center=[1000, 600]
x1=720
y1=360
outer_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#curve 1 inner h
center=[1000, 600]
x1=480
y1=120
inner_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#straight y section 1
for y in range(600, 1510, 10):
    outer_points.append((1720, y))
    inner_points.append((1480, y))

#curve 2 outer h
center=[1930, 1500]
x1=210
y1=110
outer_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 2 inner h
center=[1930, 1500]
x1=450
y1=350
inner_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 3 inner h
center=[2590, 1500]
x1=210
y1=110
inner_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#curve 3 outer h
center=[2590, 1500]
x1=450
y1=350
outer_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#curve 4 outer h
center=[3250, 1500]
x1=210
y1=110
outer_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 4 inner h
center=[3250, 1500]
x1=450
y1=350
inner_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#straight y section 2
for y in range(1500,690, -10):
    outer_points.append((3460,y))
    inner_points.append((3700,y))

#curve 5 outer h
center=[3360, 700]
x1=100
y1=60
outer_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 5 inner h
center=[3360, 700]
x1=340
y1=300
inner_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 6 inner h
center=[2920, 700]
x1=100
y1=60
inner_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 6 outer h
center=[2920, 700]
x1=340
y1=300
outer_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 7 outer h
center=[2480, 700]
x1=100
y1=60
outer_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 7 inner h
center=[2480, 700]
x1=340
y1=300
inner_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#straight y section 3
for y in range(700, 810, 10):
    outer_points.append((2380,y))
    inner_points.append((2140,y))

#filler gap
for y in range(810, 1040, 10):
    outer_points.append((2380,y))


#straight x section 1
for x in range(2380, 2040, -10):
    if x>=2140:
        outer_points.append((x,1040))
    else:
        outer_points.append((x,1040))
        inner_points.append((x, 800))

#filler gap
for x in range(2040,1820, -10):
    outer_points.append((x, 1040))

#straight y section 4
for y in range(1040, 340,-10):
    if y>=800:
        outer_points.append((1810,y))
    else:
        outer_points.append((1810, y))
        inner_points.append((2050, y))

#filler gap
for y in range(340, 120, -10):
    outer_points.append((1810,y))


#straight x section 2
for x in range(1810, 4110, 10):
    if x<=2050:
        outer_points.append((x,110))
    else:
        outer_points.append((x,110))
        inner_points.append((x,350))

#curve 8 inner v
center=[4100, 450]
y1=100
x1=60
inner_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 8 outer v
center=[4100, 450]
y1=340
x1=300
outer_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 9 outer v
center=[4100, 890]
y1=100
x1=60
outer_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 9 inner v
center=[4100, 890]
y1=340
x1=300
inner_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 10 inner v
center=[4100, 1330]
y1=100
x1=60
inner_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 10 outer v
center=[4100, 1330]
y1=340
x1=300
outer_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 11 outer v
center=[4100, 1770]
y1=100
x1=60
outer_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 11 inner v
center=[4100, 1770]
y1=340
x1=300
inner_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 12 inner v
center=[4100, 2210]
y1=100
x1=60
inner_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 12 outer v
center=[4100, 2210]
y1=340
x1=300
outer_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 13 outer v
center=[4100, 2650]
y1=100
x1=60
outer_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 13 inner v
center=[4100, 2650]
y1=340
x1=300
inner_points+=(ellipse_points_y(center, x1, y1, 1, 0))

#curve 14 inner v
center=[4100, 3090]
y1=100
x1=60
inner_points+=(ellipse_points_y(center, x1, y1, -1, 0))

#curve 14 outer v
center=[4100, 3090]
y1=340
x1=300
outer_points+=(ellipse_points_y(center, x1, y1, -1, 0))




#straight x  section 3
for x in range(4100, 3740, -10):
    outer_points.append((x,3430))
    inner_points.append((x,3190))

#filler gap
for x in range(3740, 3520, -10):
    outer_points.append((x,3430))

#straight y section 5
for y in range(3430, 2790, -10):
    if y>=3190:
        outer_points.append((3510,y))
    else:
        outer_points.append((3510,y))
        inner_points.append((3750,y))

#curve 15 outer h
center=[3260, 2800]
x1=250
y1=150
outer_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 15 inner h
center=[3260, 2800]
x1=490
y1=390
inner_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 16 inner h
center=[2520, 2800]
x1=250
y1=150
inner_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 16 outer h
center=[2520, 2800]
x1=490
y1=390
outer_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 17 outer h
center=[1780, 2800]
x1=250
y1=150
outer_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 17 inner h
center=[1780, 2800]
x1=490
y1=390
inner_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 18 inner h
center=[1040, 2800]
x1=250
y1=150
inner_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 18 outer h
center=[1040, 2800]
x1=490
y1=390
outer_points+=(ellipse_points_x(center, x1, y1, 1, 1))



#straight y section 6
for y in range(2800, 1790, -10):
    outer_points.append((550,y))
    inner_points.append((790,y))

#filler gap
for y in range(1790, 1550, -10):
    inner_points.append((790, y))

#straight x section 4
for x in range(790, 510, -10):
    if x>=550:
        inner_points.append((x,1540))
    else:
        outer_points.append((x,1800))
        inner_points.append((x,1540))

#filler gap
for x in range(510, 290, -10):
    outer_points.append((x,1800))

#straight y section 7
for y in range(1800, 840, -10):
    if y>=1540:
        outer_points.append((280,y))
    else:
        outer_points.append((280,y))
        inner_points.append((520,y))



#function to delete points that are the same and adjacent
for x in range(len(outer_points)-1, 0, -1):
    if outer_points[x]==outer_points[x-1]:
        del outer_points[x]

for x in range(len(inner_points)-1, 0, -1):
    if inner_points[x]==inner_points[x-1]:
        del inner_points[x]



