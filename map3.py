import pygame
import math
from map1 import ellipse_points_x, ellipse_points_y
from npc_car import trial_npc

npc_car1 = trial_npc("red_car.png", [1300, 3070], -180, 3, 6, "right", "npc car1", 0,0)
npc_car2 = trial_npc("red_car.png", [1300, 3170], -180, 3, 6, "left", "npc car2",0,0)


def checker_count(car):
    if (car.pos[0]>=1200 and car.pos[0]<=1210) and (car.pos[1]>=3000 and car.pos[1]<=3240):
        car.checker=car.laps
        print(car.checker)

def lap_checker(car):
    if (car.pos[0]>=1290 and car.pos[0]<1300) and (car.pos[1]>=3000 and car.pos[1]<=3240):
        car.laps=car.checker+1
        print(car.laps)
    if car.laps==3:
        return True
    else:
        return False

inner_points, outer_points, obstacle_points, checkpoints= [],[],[],[]
track_width=5000
track_height=4000

#end of straight
for y in range(1010, 590, -10):
    outer_points.append((280, y))
    inner_points.append((520, y))

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
for y in range(600, 1010, 10):
    outer_points.append((1720, y))
    inner_points.append((1480, y))

obstacle_points.append([])
#obstacle 1
for x in range(80):
    obstacle_points[0].append((math.cos(((x*math.pi)/40))*30+1600,math.sin(((x*math.pi)/40))*30+800 ))

#curve 2 inner h
center=[1930, 1000]
x1=450
y1=350
inner_points+=(ellipse_points_x(center, x1, y1, 1, 0))

obstacle_points.append([])
#obstacle 2
for x in range(80):
    obstacle_points[1].append((math.cos(((x*math.pi)/40))*30+1930,math.sin(((x*math.pi)/40))*30+1235 ))


#curve 2 outer h
center=[1930, 1000]
x1=210
y1=110
outer_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#straight y section 2
for y in range(1000, 590, -10):
    outer_points.append((2140, y))
    inner_points.append((2380, y))

#filler gap
for y in range(590, 360, -10):
    outer_points.append((2140, y))

#straight x section 1
for x in range(2140, 3010, 10):
    if x<=2380:
        outer_points.append((x,360))
    else:
        outer_points.append((x,360))
        inner_points.append((x,600))

obstacle_points.append([])
#obstacle 3
for y in range(360, 450, 10):
    obstacle_points[2].append((2300, y))
for x in range(2300, 2390, 10):
    obstacle_points[2].append((x, 440))
for y in range(440, 350, -10):
    obstacle_points[2].append((2380, y))

#filler gap
for x in range(3010, 3240, 10):
    outer_points.append((x, 360))

#straight y section 3
for y in range(360, 1510, 10):
    if y<=600:
        outer_points.append((3240, y))
    else:
        outer_points.append((3240, y))
        inner_points.append((3000, y))

obstacle_points.append([])
#obstacle 4
for y in range(800, 960, 10):
    obstacle_points[3].append((3090, y))
for x in range(3090, 3160, 10):
    obstacle_points[3].append((x, 950))
for y in range(950, 790, -10):
    obstacle_points[3].append((3150, y))
for x in range(3150, 3080, -10):
    obstacle_points[3].append((x, 800))

#filler gap
for y in range(1510, 1740, 10):
    outer_points.append((3240, y))

obstacle_points.append([])
#obstacle 5
for x in range(80):
    obstacle_points[4].append((math.cos(((x*math.pi)/40))*30+3150,math.sin(((x*math.pi)/40))*30+1650 ))

#straight x section 2
for x in range(3240, 2730, -10):
    if x>=3000:
        outer_points.append((x, 1740))
    else:
        outer_points.append((x, 1740))
        inner_points.append((x, 1500))

#filler gap
for x in range(2730, 2500, -10):
    inner_points.append((x, 1500))

#straight y section 4
for y in range(1500, 2010,10):
    if y<=1740:
        inner_points.append((2490, y))
    else:
        inner_points.append((2490, y))
        outer_points.append((2730, y))

#curve 3 outer h
center=[2330, 2000]
x1=400
y1=290
outer_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 3 inner h
center=[2330, 2000]
x1=160
y1=50
inner_points+=(ellipse_points_x(center, x1, y1, 1, 1))

#curve 4 inner h
center=[1770, 2000]
x1=400
y1=290
inner_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#curve 4 outer h
center=[1770, 2000]
x1=160
y1=50
outer_points+=(ellipse_points_x(center, x1, y1, -1, 1))

#straight y section 5

for y in range(2000, 2610, 10):
    outer_points.append((1610, y))
    inner_points.append((1370, y))

obstacle_points.append([])
#obstacle 6
for y in range(2200, 2410, 10):
    obstacle_points[5].append((1460, y))
for x in range(1460, 1530, 10):
    obstacle_points[5].append((x, 2400))
for y in range(2400, 2190, -10):
    obstacle_points[5].append((1520, y))
for x in range(1520, 1450, -10):
    obstacle_points[5].append((x, 2200))

#curve 5 inner h
center=[1870, 2600]
x1=500
y1=330
inner_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 5 outer h
center=[1870, 2600]
x1=260
y1=90
outer_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 6 outer h
center=[2630, 2600]
x1=500
y1=330
outer_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#curve 6 inner h
center=[2630, 2600]
x1=260
y1=90
inner_points+=(ellipse_points_x(center, x1, y1, -1, 0))

#curve 7 inner h
center=[3390, 2600]
x1=500
y1=330
inner_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#curve 7 outer h
center=[3390, 2600]
x1=260
y1=90
outer_points+=(ellipse_points_x(center, x1, y1, 1, 0))

#straight y section 6
for y in range(2600, 1490, -10):
    outer_points.append((3650, y))
    inner_points.append((3890, y))

obstacle_points.append([])
#obstacle 7
for x in range(3650, 3720, 10):
    obstacle_points[6].append((x, 2400))
for y in range(2400, 2330, -10):
    obstacle_points[6].append((3710, y))
for x in range(3710, 3640, -10):
    obstacle_points[6].append((x, 2340))

obstacle_points.append([])
#obstacle 8
for x in range(3890, 3840, -10):
    obstacle_points[7].append((x, 1800))
for y in range(1800, 1870, 10):
    obstacle_points[7].append((3850, y))
for x in range(3850, 3900, 10):
    obstacle_points[7].append((x, 1860))


#filler gap
for y in range(1490, 1260, -10):
    outer_points.append((3650, y))

#straight x section 3
for x in range(3650, 4360, 10):
    if x<=3890:
        outer_points.append((x, 1260))
    else:
        outer_points.append((x, 1260))
        inner_points.append((x, 1500))

#filler gap
for x in range(4360, 4590, 10):
    outer_points.append((x, 1260))

#straight y section 7
for y in range(1260, 1820, 10):
    if y<=1500:
        outer_points.append((4590, y))
    else:
        outer_points.append((4590, y))
        inner_points.append((4350, y))

#filler gap
for y in range(1820, 2050, 10):
    outer_points.append((4590, y))

#straight x section 4
for x in range(4590, 4210, -10):
    if x>=4350:
        outer_points.append((x, 2050))
    else:
        outer_points.append((x, 2050))
        inner_points.append((x, 1810))

#filler gap
for x in range(4210, 3980, -10):
    inner_points.append((x, 1810))

#straight y section 8
for y in range(1810, 2370, 10):
    if y<=2050:
        inner_points.append((3980, y))
    else:
        inner_points.append((3980, y))
        outer_points.append((4220, y))

#filler gap
for y in range(2370, 2600, 10):
    inner_points.append((3980, y))

#straight x section 5
for x in range(3980, 4350, 10):
    if x<=4220:
        inner_points.append((x, 2600))
    else:
        inner_points.append((x, 2600))
        outer_points.append((x, 2360))

#filler gap
for x in range(4350, 4590, 10):
    outer_points.append((x, 2360))

#straight y section 9
for y in range(2360, 3010, 10):
    if y<=2600:
        outer_points.append((4590, y))
    else:
        outer_points.append((4590, y))
        inner_points.append((4350, y))

#filler gap
for y in range(3010, 3240, 10):
    outer_points.append((4590, y))

#straight x section 6
for x in range(4590, 3710, -10):
    if x>=4350:
        outer_points.append((x, 3240))
    else:
        outer_points.append((x, 3240))
        inner_points.append((x, 3000))

obstacle_points.append([])
#obstacle 9
for x in range(4100, 4010, -10):
    obstacle_points[8].append((x, 3090))
for y in range(3090, 3160, 10):
    obstacle_points[8].append((4020, y))
for x in range(4020, 4110, 10):
    obstacle_points[8].append((x, 3150))
for y in range(3150, 3080, -10):
    obstacle_points[8].append((4110, y))


#filler gap
for x in range(3710, 3480, -10):
    inner_points.append((x, 3000))

#straigt y section 10
for y in range(3000, 3410, 10):
    if y<=3240:
        inner_points.append((3480, y))
    else:
        inner_points.append((3480, y))
        outer_points.append((3720, y))


#filler gap
for y in range(3410, 3640, 10):
    outer_points.append((3720, y))

#straight x section 7
for x in range(3720, 3030, -10):
    if x>=3480:
        outer_points.append((x, 3640))
    else:
        outer_points.append((x, 3640))
        inner_points.append((x, 3400))

#filler gap
for x in range(3030, 2800, -10):
    outer_points.append((x, 3640))

#straight y section 11
for y in range(3640, 3230, -10):
    if y>=3400:
        outer_points.append((2800, y))
    else:
        outer_points.append((2800, y))
        inner_points.append((3040, y))

#filler gap
for y in range(3230, 3000, -10):
    inner_points.append((3040, y))

#straight x section 8
for x in range(3040, 2510, -10):
    if x>=2800:
        inner_points.append((x, 3000))
    else:
        inner_points.append((x, 3000))
        outer_points.append((x, 3240))


#filler gap
for x in range(2510, 2280, -10):
    inner_points.append((x, 3000))

#straigt y section 12
for y in range(3000, 3410, 10):
    if y<=3240:
        inner_points.append((2280, y))
    else:
        inner_points.append((2280, y))
        outer_points.append((2520, y))

#filler gap
for y in range(3410, 3640, 10):
    outer_points.append((2520, y))

#straight x section 9
for x in range(2520, 1830, -10):
    if x>=2280:
        outer_points.append((x, 3640))
    else:
        outer_points.append((x, 3640))
        inner_points.append((x, 3400))

#filler gap
for x in range(1830, 1600, -10):
    outer_points.append((x, 3640))

#straight y section 13
for y in range(3640, 3230, -10):
    if y>=3400:
        outer_points.append((1600, y))
    else:
        outer_points.append((1600, y))
        inner_points.append((1840, y))

#filler gap
for y in range(3230, 3000, -10):
    inner_points.append((1840, y))

#straight x section 10
for x in range(1840, 530, -10):
    if x>=1600:
        inner_points.append((x, 3000))
    else:
        inner_points.append((x, 3000))
        outer_points.append((x, 3240))
#filler gap
for x in range(530, 280, -10):
    outer_points.append((x, 3240))

#straight y section 14:
for y in range(3240, 1010, -10):
    if y>=3000:
        outer_points.append((280, y))
    else:
        outer_points.append((280, y))
        inner_points.append((520, y))

obstacle_points.append([])
#obstacle 10
for x in range(80):
    obstacle_points[9].append((math.cos(((x*math.pi)/40))*30+400,math.sin(((x*math.pi)/40))*30+2500 ))


obstacle_points.append([])
#obstacle 11
for x in range(280, 340, 10):
    obstacle_points[10].append((x,1700 ))
for y in range(1700, 1630, -10):
    obstacle_points[10].append((330, y))
for x in range(330, 270, -10):
    obstacle_points[10].append((x, 1640))


obstacle_points.append([])
#obstacle 12
for x in range(520, 470, -10):
    obstacle_points[11].append((x, 1300))
for y in range(1300, 1360, 10):
    obstacle_points[11].append((480, y))
for x in range(480, 530, 10):
    obstacle_points[11].append((x, 1360))





#function to delete points that are the same and adjacent
for x in range(len(outer_points)-1, 0, -1):
    if outer_points[x]==outer_points[x-1]:
        del outer_points[x]

for x in range(len(inner_points)-1, 0, -1):
    if inner_points[x]==inner_points[x-1]:
        del inner_points[x]
