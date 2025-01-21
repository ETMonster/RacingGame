import pygame
import math
from npc_car import trial_npc


npc_car1 = trial_npc("red_car.png", [450, 2250], -90, 3, 6, "right", "npc car1", 0,0)
npc_car2 = trial_npc("red_car.png", [350, 2250], -90, 3, 6, "left", "npc car2",0,0)

def checker_count(car):
    if (car.pos[0]>=280 and car.pos[0]<=520) and (car.pos[1]>=2300 and car.pos[1]<=2310):
        car.checker=car.laps
        print(car.checker)

def lap_checker(car):
    if (car.pos[0]>=280 and car.pos[0]<520) and (car.pos[1]>=2240 and car.pos[1]<=2250):
        car.laps=car.checker+1
        print(car.laps)
    if car.laps==3:
        return True
    else:
        return False


#ellipse function used in previous week
def ellipse_points_x(center, x, y, direction, sort): #direction =-1 draw upper half direction=0 draw lower half
    coordinates = []
    for i in range(180):
        rad = direction*(math.pi /180) * i
        a = center[0] + x * math.cos(rad)
        b = center[1] + y * math.sin(rad)
        coordinates.append((a, b))
    if sort==0:
        coordinates.sort(key=lambda coordinates:coordinates[0]) #sort by increasing first index value to ensure proper segments
    if sort==1:
        coordinates.sort(key=lambda coordinates: coordinates[0], reverse=True) #sort by decreasing order
    return coordinates

# same function but for when the ellipse is rotated 90 deg
def ellipse_points_y(center, x, y, direction, sort):
    coordinates = []
    for i in range(180):
        rad = 2*(math.pi / 180) * i
        a = center[0] + x * math.cos(rad)
        b = center[1] + y * math.sin(rad)

        if direction==1 and a <= center[0]: #if direction=1 then only draw left half
            coordinates.append((a, b))
        elif direction==-1 and a >= center[0]: #if direction=-1 then only draw right half
            coordinates.append((a, b))

    if sort==0:
        coordinates.sort(key=lambda coordinates:coordinates[1]) #sort by increasing y value
    if sort==1:
        coordinates.sort(key=lambda coordinates: coordinates[1], reverse=True) #sort by decreasing y value
    return coordinates


inner_points, outer_points,obstacle_points, checkpoints=[],[],[],[]
checkpoints.append(pygame.Rect(1480, 800, 240, 30))
checkpoints.append(pygame.Rect(1300, 1940, 30, 240))
checkpoints.append(pygame.Rect(2700, 2340, 30, 240))
checkpoints.append(pygame.Rect(1000, 2600, 30, 240))
finish_line=pygame.Rect(280,2240, 240, 10)

#filler test
for y in range(2830, 2600,-10):
    outer_points.append((280,y))

obstacle_points.append([])
#obstacle 1
for y in range(1000, 840, -10):
    obstacle_points[0].append((370,y))
for x in range(370,440, 10):
    obstacle_points[0].append((x,850))
for y in range(850, 1010, 10):
    obstacle_points[0].append((430,y))
for x in range(430, 360, -10):
    obstacle_points[0].append((x,1000))


#end of straight y section 1 60 points
for y in range(2600, 590, -10):
    outer_points.append((280, y))
    inner_points.append((520, y))

#curve 1 inner (smaller ellipse) h #180 points
center=[1000, 600]
x1=480
y1=120
inner_points+=(ellipse_points_x(center, x1, y1, -1,0))

#curve 1 outer (larger ellipse) h
center=[1000, 600]
x1=720
y1=360
outer_points+=(ellipse_points_x(center, x1, y1, -1,0))

#straight y section 2 40 points
for y in range(600, 1010, 10):
    outer_points.append((1720, y))
    inner_points.append((1480, y))


#filler for line gap 1
for y in range(1010, 1250, 10):
    outer_points.append((1720, y))

obstacle_points.append([])
#obstacle 2
for x in range(80):
    obstacle_points[1].append((math.cos(((x*math.pi)/40))*30+1300,math.sin(((x*math.pi)/40))*30+1120 ))

#straight x section 1 72 points for outer 47 for inner
for x in range(1720, 1090, -10):
    if (x>=1480) and (x<=1720):
        outer_points.append((x, 1240))
    elif x<1480:
        outer_points.append((x, 1240))
        inner_points.append((x, 1000))

#curve 2 outer (smaller ellipse) v #180 points
center=[1100,1590]
x1=200
y1=350
outer_points+=(ellipse_points_y(center, x1, y1, 1,0))
#curve 2 inner (larger ellipse) v
center=[1100,1590]
x1=440
y1=590
inner_points+=(ellipse_points_y(center, x1, y1, 1,0))

#straight x section 2
for x in range(1110, 1910, 10):
    outer_points.append((x, 1940))
    inner_points.append((x, 2180))


#filler for line gap 2
for x in range(1910, 2150, 10):
    inner_points.append((x,2180))

obstacle_points.append([])
#obstacle 3
for x in range(80):
    obstacle_points[2].append((math.cos(((x*math.pi)/40))*30+2070,math.sin(((x*math.pi)/40))*30+2060 ))



#straight y section 3
for y in range(2180, 1190, -10):
    if y<=2180 and y>=1940:
        inner_points.append((2140, y))
    else:
        inner_points.append((2140, y))
        outer_points.append((1900, y))

#filler for line gap 3
for y in range (1190, 950, -10):
    outer_points.append((1900, y))

#straight x section 3
for x in range(1900, 2710, 10):
    if x>=1900 and x<=2140:
        outer_points.append((x, 960))
    else:
        outer_points.append((x, 960))
        inner_points.append((x, 1200))

#curve 3 outer (bigger ellipse) v
center=[2700, 1450]
x1=350
y1=490
outer_points+=(ellipse_points_y(center, x1, y1, -1,0))

#curve 3 inner (smaller ellipse) v
center=[2700, 1450]
x1=110
y1=250
inner_points+=(ellipse_points_y(center, x1, y1, -1,0))

#straight x section 4
for x in range(2700, 2640, -10):
    outer_points.append((x, 1940))
    inner_points.append((x, 1700))

#curve 4 outer (smaller ellipse) v
center=[2650, 2140]
x1=110
y1=200
outer_points+=(ellipse_points_y(center, x1, y1, 1,0))

#curve 4 inner (bigger ellipse) v
center=[2650, 2140]
x1=350
y1=440
inner_points+=(ellipse_points_y(center, x1, y1, 1,0))

#straight x section 5
for x in range(2650, 3010, 10):
    outer_points.append((x, 2340))
    inner_points.append((x, 2580))


#filler test gap 1
for x in range(3010, 3250, 10):
    outer_points.append((x, 2340))

#straight y section 4
for y in range(2340, 2610, 10):
    if y>=2340 and y<=2580:
        outer_points.append((3240,y))
    else:
        outer_points.append((3240,y))
        inner_points.append((3000,y))

#filler test gap 2
for y in range(2610, 2850, 10):
    outer_points.append((3240,y))

#straight x section 6
for x in range (3240, 270, -10):
    if (x>=3000 and x<=3240) or (x>=280 and x<=520):
        outer_points.append((x, 2840))
    else:
        outer_points.append((x, 2840))
        inner_points.append((x, 2600))

obstacle_points.append([])
#obstacle 4
for y in range(2840, 2750, -10):
    obstacle_points[3].append((2500, y))
for x in range(2500, 2410, -10):
    obstacle_points[3].append((x, 2760))
for y in range(2760, 2850, 10):
    obstacle_points[3].append((2420, y))

obstacle_points.append([])
#obstacle 5
for y in range(2600, 2690, 10):
    obstacle_points[4].append((2300, y))
for x in range(2300, 2210, -10):
    obstacle_points[4].append((x, 2680))
for y in range(2680, 2590, -10):
    obstacle_points[4].append((2200, y))

obstacle_points.append([])
#obstacle 6
for x in range(80):
    obstacle_points[5].append((math.cos(((x*math.pi)/40))*30+1400,math.sin(((x*math.pi)/40))*30+2760 ))


#function to delete points that are the same and adjacent
for x in range(len(outer_points)-1, 0, -1):
    if outer_points[x]==outer_points[x-1]:
        del outer_points[x]

for x in range(len(inner_points)-1, 0, -1):
    if inner_points[x]==inner_points[x-1]:
        del inner_points[x]
