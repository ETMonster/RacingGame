import pygame
from constants import *
import math


def map_1():
    inner_points, outer_points, obstacle_points, checkpoints = [], [], [], []
    checkpoints.append(pygame.Rect(1000, 2600, 30, 240)) #facing left
    checkpoints.append(pygame.Rect(1480, 800, 240, 30)) #facing down
    checkpoints.append(pygame.Rect(1300, 1940, 30, 240)) #facing right
    checkpoints.append(pygame.Rect(2700, 2340, 30, 240)) #facing right
    finish_line = pygame.Rect(1800, 2600, 30, 240)

    # filler test
    for y in range(2830, 2600, -10):
        outer_points.append((280, y))

    obstacle_points.append([])
    # obstacle 1
    for y in range(1000, 840, -10):
        obstacle_points[0].append((370, y))
    for x in range(370, 440, 10):
        obstacle_points[0].append((x, 850))
    for y in range(850, 1010, 10):
        obstacle_points[0].append((430, y))
    for x in range(430, 360, -10):
        obstacle_points[0].append((x, 1000))

    # end of straight y section 1 60 points
    for y in range(2600, 590, -10):
        outer_points.append((280, y))
        inner_points.append((520, y))

    # curve 1 inner (smaller ellipse) h #180 points
    center = [1000, 600]
    x1 = 480
    y1 = 120
    inner_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 1 outer (larger ellipse) h
    center = [1000, 600]
    x1 = 720
    y1 = 360
    outer_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # straight y section 2 40 points
    for y in range(600, 1010, 10):
        outer_points.append((1720, y))
        inner_points.append((1480, y))

    # filler for line gap 1
    for y in range(1010, 1250, 10):
        outer_points.append((1720, y))

    obstacle_points.append([])
    # obstacle 2
    for x in range(80):
        obstacle_points[1].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 1300, math.sin(((x * math.pi) / 40)) * 30 + 1120))

    # straight x section 1 72 points for outer 47 for inner
    for x in range(1720, 1090, -10):
        if (x >= 1480) and (x <= 1720):
            outer_points.append((x, 1240))
        elif x < 1480:
            outer_points.append((x, 1240))
            inner_points.append((x, 1000))

    # curve 2 outer (smaller ellipse) v #180 points
    center = [1100, 1590]
    x1 = 200
    y1 = 350
    outer_points += (ellipse_points_y(center, x1, y1, 1, 0))
    # curve 2 inner (larger ellipse) v
    center = [1100, 1590]
    x1 = 440
    y1 = 590
    inner_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # straight x section 2
    for x in range(1110, 1910, 10):
        outer_points.append((x, 1940))
        inner_points.append((x, 2180))

    # filler for line gap 2
    for x in range(1910, 2150, 10):
        inner_points.append((x, 2180))

    obstacle_points.append([])
    # obstacle 3
    for x in range(80):
        obstacle_points[2].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 2070, math.sin(((x * math.pi) / 40)) * 30 + 2060))

    # straight y section 3
    for y in range(2180, 1190, -10):
        if y <= 2180 and y >= 1940:
            inner_points.append((2140, y))
        else:
            inner_points.append((2140, y))
            outer_points.append((1900, y))

    # filler for line gap 3
    for y in range(1190, 950, -10):
        outer_points.append((1900, y))

    # straight x section 3
    for x in range(1900, 2710, 10):
        if x >= 1900 and x <= 2140:
            outer_points.append((x, 960))
        else:
            outer_points.append((x, 960))
            inner_points.append((x, 1200))

    # curve 3 outer (bigger ellipse) v
    center = [2700, 1450]
    x1 = 350
    y1 = 490
    outer_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 3 inner (smaller ellipse) v
    center = [2700, 1450]
    x1 = 110
    y1 = 250
    inner_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # straight x section 4
    for x in range(2700, 2640, -10):
        outer_points.append((x, 1940))
        inner_points.append((x, 1700))

    # curve 4 outer (smaller ellipse) v
    center = [2650, 2140]
    x1 = 110
    y1 = 200
    outer_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 4 inner (bigger ellipse) v
    center = [2650, 2140]
    x1 = 350
    y1 = 440
    inner_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # straight x section 5
    for x in range(2650, 3010, 10):
        outer_points.append((x, 2340))
        inner_points.append((x, 2580))

    # filler test gap 1
    for x in range(3010, 3250, 10):
        outer_points.append((x, 2340))

    # straight y section 4
    for y in range(2340, 2610, 10):
        if y >= 2340 and y <= 2580:
            outer_points.append((3240, y))
        else:
            outer_points.append((3240, y))
            inner_points.append((3000, y))

    # filler test gap 2
    for y in range(2610, 2850, 10):
        outer_points.append((3240, y))

    # straight x section 6
    for x in range(3240, 270, -10):
        if (x >= 3000 and x <= 3240) or (x >= 280 and x <= 520):
            outer_points.append((x, 2840))
        else:
            outer_points.append((x, 2840))
            inner_points.append((x, 2600))

    obstacle_points.append([])
    # obstacle 4
    for y in range(2840, 2750, -10):
        obstacle_points[3].append((2500, y))
    for x in range(2500, 2410, -10):
        obstacle_points[3].append((x, 2760))
    for y in range(2760, 2850, 10):
        obstacle_points[3].append((2420, y))

    obstacle_points.append([])
    # obstacle 5
    for y in range(2600, 2690, 10):
        obstacle_points[4].append((2300, y))
    for x in range(2300, 2210, -10):
        obstacle_points[4].append((x, 2680))
    for y in range(2680, 2590, -10):
        obstacle_points[4].append((2200, y))

    obstacle_points.append([])
    # obstacle 6
    for x in range(80):
        obstacle_points[5].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 1400, math.sin(((x * math.pi) / 40)) * 30 + 2760))

    # function to delete points that are the same and adjacent
    for x in range(len(outer_points) - 1, 0, -1):
        if outer_points[x] == outer_points[x - 1]:
            del outer_points[x]

    for x in range(len(inner_points) - 1, 0, -1):
        if inner_points[x] == inner_points[x - 1]:
            del inner_points[x]

    return {
        'outer': outer_points,
        'inner': inner_points,
        'obstacle': obstacle_points,
        'checkpoint': checkpoints,
        'finish': finish_line
    }
def map_2():
    inner_points, outer_points, obstacle_points, checkpoints = [], [], [], []

    checkpoints.append(pygame.Rect(3900, 3190, 30, 240)) #facing left
    checkpoints.append(pygame.Rect(550, 2600, 240, 30)) #facing up
    checkpoints.append(pygame.Rect(1480, 800, 240, 30)) #facing down
    checkpoints.append(pygame.Rect(2100, 800, 30, 240)) #facing left
    finish_line = pygame.Rect(3280, 110, 30, 240)

    # end of straight
    for y in range(840, 590, -10):
        outer_points.append((280, y))
        inner_points.append((520, y))

    # curve 1 outer h
    center = [1000, 600]
    x1 = 720
    y1 = 360
    outer_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 1 inner h
    center = [1000, 600]
    x1 = 480
    y1 = 120
    inner_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # straight y section 1
    for y in range(600, 1510, 10):
        outer_points.append((1720, y))
        inner_points.append((1480, y))

    # curve 2 outer h
    center = [1930, 1500]
    x1 = 210
    y1 = 110
    outer_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 2 inner h
    center = [1930, 1500]
    x1 = 450
    y1 = 350
    inner_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 3 inner h
    center = [2590, 1500]
    x1 = 210
    y1 = 110
    inner_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 3 outer h
    center = [2590, 1500]
    x1 = 450
    y1 = 350
    outer_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 4 outer h
    center = [3250, 1500]
    x1 = 210
    y1 = 110
    outer_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 4 inner h
    center = [3250, 1500]
    x1 = 450
    y1 = 350
    inner_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # straight y section 2
    for y in range(1500, 690, -10):
        outer_points.append((3460, y))
        inner_points.append((3700, y))

    # curve 5 outer h
    center = [3360, 700]
    x1 = 100
    y1 = 60
    outer_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 5 inner h
    center = [3360, 700]
    x1 = 340
    y1 = 300
    inner_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 6 inner h
    center = [2920, 700]
    x1 = 100
    y1 = 60
    inner_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 6 outer h
    center = [2920, 700]
    x1 = 340
    y1 = 300
    outer_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 7 outer h
    center = [2480, 700]
    x1 = 100
    y1 = 60
    outer_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 7 inner h
    center = [2480, 700]
    x1 = 340
    y1 = 300
    inner_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # straight y section 3
    for y in range(700, 810, 10):
        outer_points.append((2380, y))
        inner_points.append((2140, y))

    # filler gap
    for y in range(810, 1040, 10):
        outer_points.append((2380, y))

    # straight x section 1
    for x in range(2380, 2040, -10):
        if x >= 2140:
            outer_points.append((x, 1040))
        else:
            outer_points.append((x, 1040))
            inner_points.append((x, 800))

    # filler gap
    for x in range(2040, 1820, -10):
        outer_points.append((x, 1040))

    # straight y section 4
    for y in range(1040, 340, -10):
        if y >= 800:
            outer_points.append((1810, y))
        else:
            outer_points.append((1810, y))
            inner_points.append((2050, y))

    # filler gap
    for y in range(340, 120, -10):
        outer_points.append((1810, y))

    # straight x section 2
    for x in range(1810, 4110, 10):
        if x <= 2050:
            outer_points.append((x, 110))
        else:
            outer_points.append((x, 110))
            inner_points.append((x, 350))

    # curve 8 inner v
    center = [4100, 450]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 8 outer v
    center = [4100, 450]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 9 outer v
    center = [4100, 890]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 9 inner v
    center = [4100, 890]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 10 inner v
    center = [4100, 1330]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 10 outer v
    center = [4100, 1330]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 11 outer v
    center = [4100, 1770]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 11 inner v
    center = [4100, 1770]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 12 inner v
    center = [4100, 2210]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 12 outer v
    center = [4100, 2210]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 13 outer v
    center = [4100, 2650]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 13 inner v
    center = [4100, 2650]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points_y(center, x1, y1, 1, 0))

    # curve 14 inner v
    center = [4100, 3090]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # curve 14 outer v
    center = [4100, 3090]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points_y(center, x1, y1, -1, 0))

    # straight x section 3
    for x in range(4100, 3740, -10):
        outer_points.append((x, 3430))
        inner_points.append((x, 3190))

    # filler gap
    for x in range(3740, 3520, -10):
        outer_points.append((x, 3430))

    # straight y section 5
    for y in range(3430, 2790, -10):
        if y >= 3190:
            outer_points.append((3510, y))
        else:
            outer_points.append((3510, y))
            inner_points.append((3750, y))

    # curve 15 outer h
    center = [3260, 2800]
    x1 = 250
    y1 = 150
    outer_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 15 inner h
    center = [3260, 2800]
    x1 = 490
    y1 = 390
    inner_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 16 inner h
    center = [2520, 2800]
    x1 = 250
    y1 = 150
    inner_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 16 outer h
    center = [2520, 2800]
    x1 = 490
    y1 = 390
    outer_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 17 outer h
    center = [1780, 2800]
    x1 = 250
    y1 = 150
    outer_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 17 inner h
    center = [1780, 2800]
    x1 = 490
    y1 = 390
    inner_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 18 inner h
    center = [1040, 2800]
    x1 = 250
    y1 = 150
    inner_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 18 outer h
    center = [1040, 2800]
    x1 = 490
    y1 = 390
    outer_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # straight y section 6
    for y in range(2800, 1790, -10):
        outer_points.append((550, y))
        inner_points.append((790, y))

    # filler gap
    for y in range(1790, 1550, -10):
        inner_points.append((790, y))

    # straight x section 4
    for x in range(790, 510, -10):
        if x >= 550:
            inner_points.append((x, 1540))
        else:
            outer_points.append((x, 1800))
            inner_points.append((x, 1540))

    # filler gap
    for x in range(510, 290, -10):
        outer_points.append((x, 1800))

    # straight y section 7
    for y in range(1800, 840, -10):
        if y >= 1540:
            outer_points.append((280, y))
        else:
            outer_points.append((280, y))
            inner_points.append((520, y))

    # function to delete points that are the same and adjacent
    for x in range(len(outer_points) - 1, 0, -1):
        if outer_points[x] == outer_points[x - 1]:
            del outer_points[x]

    for x in range(len(inner_points) - 1, 0, -1):
        if inner_points[x] == inner_points[x - 1]:
            del inner_points[x]

    return {
        'outer': outer_points,
        'inner': inner_points,
        'obstacle': obstacle_points,
        'checkpoint': checkpoints,
        'finish': finish_line
    }
def map_3():
    inner_points, outer_points, obstacle_points, checkpoints = [], [], [], []

    checkpoints.append(pygame.Rect(280, 800, 240, 30)) #facing up
    checkpoints.append(pygame.Rect(2800, 1500, 30, 240)) #facing left
    checkpoints.append(pygame.Rect(3650, 2000, 240, 30)) #facing up
    checkpoints.append(pygame.Rect(4350, 2800, 240, 30)) #facing down
    finish_line = pygame.Rect(1020, 3000, 30, 240)

    # end of straight
    for y in range(1010, 590, -10):
        outer_points.append((280, y))
        inner_points.append((520, y))

    # curve 1 outer h
    center = [1000, 600]
    x1 = 720
    y1 = 360
    outer_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 1 inner h
    center = [1000, 600]
    x1 = 480
    y1 = 120
    inner_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # straight y section 1
    for y in range(600, 1010, 10):
        outer_points.append((1720, y))
        inner_points.append((1480, y))

    obstacle_points.append([])
    # obstacle 1
    for x in range(80):
        obstacle_points[0].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 1600, math.sin(((x * math.pi) / 40)) * 30 + 800))

    # curve 2 inner h
    center = [1930, 1000]
    x1 = 450
    y1 = 350
    inner_points += (ellipse_points_x(center, x1, y1, 1, 0))

    obstacle_points.append([])
    # obstacle 2
    for x in range(80):
        obstacle_points[1].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 1930, math.sin(((x * math.pi) / 40)) * 30 + 1235))

    # curve 2 outer h
    center = [1930, 1000]
    x1 = 210
    y1 = 110
    outer_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # straight y section 2
    for y in range(1000, 590, -10):
        outer_points.append((2140, y))
        inner_points.append((2380, y))

    # filler gap
    for y in range(590, 360, -10):
        outer_points.append((2140, y))

    # straight x section 1
    for x in range(2140, 3010, 10):
        if x <= 2380:
            outer_points.append((x, 360))
        else:
            outer_points.append((x, 360))
            inner_points.append((x, 600))

    obstacle_points.append([])
    # obstacle 3
    for y in range(360, 450, 10):
        obstacle_points[2].append((2300, y))
    for x in range(2300, 2390, 10):
        obstacle_points[2].append((x, 440))
    for y in range(440, 350, -10):
        obstacle_points[2].append((2380, y))

    # filler gap
    for x in range(3010, 3240, 10):
        outer_points.append((x, 360))

    # straight y section 3
    for y in range(360, 1510, 10):
        if y <= 600:
            outer_points.append((3240, y))
        else:
            outer_points.append((3240, y))
            inner_points.append((3000, y))

    obstacle_points.append([])
    # obstacle 4
    for y in range(800, 960, 10):
        obstacle_points[3].append((3090, y))
    for x in range(3090, 3160, 10):
        obstacle_points[3].append((x, 950))
    for y in range(950, 790, -10):
        obstacle_points[3].append((3150, y))
    for x in range(3150, 3080, -10):
        obstacle_points[3].append((x, 800))

    # filler gap
    for y in range(1510, 1740, 10):
        outer_points.append((3240, y))

    obstacle_points.append([])
    # obstacle 5
    for x in range(80):
        obstacle_points[4].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 3150, math.sin(((x * math.pi) / 40)) * 30 + 1650))

    # straight x section 2
    for x in range(3240, 2730, -10):
        if x >= 3000:
            outer_points.append((x, 1740))
        else:
            outer_points.append((x, 1740))
            inner_points.append((x, 1500))

    # filler gap
    for x in range(2730, 2500, -10):
        inner_points.append((x, 1500))

    # straight y section 4
    for y in range(1500, 2010, 10):
        if y <= 1740:
            inner_points.append((2490, y))
        else:
            inner_points.append((2490, y))
            outer_points.append((2730, y))

    # curve 3 outer h
    center = [2330, 2000]
    x1 = 400
    y1 = 290
    outer_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 3 inner h
    center = [2330, 2000]
    x1 = 160
    y1 = 50
    inner_points += (ellipse_points_x(center, x1, y1, 1, 1))

    # curve 4 inner h
    center = [1770, 2000]
    x1 = 400
    y1 = 290
    inner_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # curve 4 outer h
    center = [1770, 2000]
    x1 = 160
    y1 = 50
    outer_points += (ellipse_points_x(center, x1, y1, -1, 1))

    # straight y section 5

    for y in range(2000, 2610, 10):
        outer_points.append((1610, y))
        inner_points.append((1370, y))

    obstacle_points.append([])
    # obstacle 6
    for y in range(2200, 2410, 10):
        obstacle_points[5].append((1460, y))
    for x in range(1460, 1530, 10):
        obstacle_points[5].append((x, 2400))
    for y in range(2400, 2190, -10):
        obstacle_points[5].append((1520, y))
    for x in range(1520, 1450, -10):
        obstacle_points[5].append((x, 2200))

    # curve 5 inner h
    center = [1870, 2600]
    x1 = 500
    y1 = 330
    inner_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 5 outer h
    center = [1870, 2600]
    x1 = 260
    y1 = 90
    outer_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 6 outer h
    center = [2630, 2600]
    x1 = 500
    y1 = 330
    outer_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 6 inner h
    center = [2630, 2600]
    x1 = 260
    y1 = 90
    inner_points += (ellipse_points_x(center, x1, y1, -1, 0))

    # curve 7 inner h
    center = [3390, 2600]
    x1 = 500
    y1 = 330
    inner_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # curve 7 outer h
    center = [3390, 2600]
    x1 = 260
    y1 = 90
    outer_points += (ellipse_points_x(center, x1, y1, 1, 0))

    # straight y section 6
    for y in range(2600, 1490, -10):
        outer_points.append((3650, y))
        inner_points.append((3890, y))

    obstacle_points.append([])
    # obstacle 7
    for x in range(3650, 3720, 10):
        obstacle_points[6].append((x, 2400))
    for y in range(2400, 2330, -10):
        obstacle_points[6].append((3710, y))
    for x in range(3710, 3640, -10):
        obstacle_points[6].append((x, 2340))

    obstacle_points.append([])
    # obstacle 8
    for x in range(3890, 3840, -10):
        obstacle_points[7].append((x, 1800))
    for y in range(1800, 1870, 10):
        obstacle_points[7].append((3850, y))
    for x in range(3850, 3900, 10):
        obstacle_points[7].append((x, 1860))

    # filler gap
    for y in range(1490, 1260, -10):
        outer_points.append((3650, y))

    # straight x section 3
    for x in range(3650, 4360, 10):
        if x <= 3890:
            outer_points.append((x, 1260))
        else:
            outer_points.append((x, 1260))
            inner_points.append((x, 1500))

    # filler gap
    for x in range(4360, 4590, 10):
        outer_points.append((x, 1260))

    # straight y section 7
    for y in range(1260, 1820, 10):
        if y <= 1500:
            outer_points.append((4590, y))
        else:
            outer_points.append((4590, y))
            inner_points.append((4350, y))

    # filler gap
    for y in range(1820, 2050, 10):
        outer_points.append((4590, y))

    # straight x section 4
    for x in range(4590, 4210, -10):
        if x >= 4350:
            outer_points.append((x, 2050))
        else:
            outer_points.append((x, 2050))
            inner_points.append((x, 1810))

    # filler gap
    for x in range(4210, 3980, -10):
        inner_points.append((x, 1810))

    # straight y section 8
    for y in range(1810, 2370, 10):
        if y <= 2050:
            inner_points.append((3980, y))
        else:
            inner_points.append((3980, y))
            outer_points.append((4220, y))

    # filler gap
    for y in range(2370, 2600, 10):
        inner_points.append((3980, y))

    # straight x section 5
    for x in range(3980, 4350, 10):
        if x <= 4220:
            inner_points.append((x, 2600))
        else:
            inner_points.append((x, 2600))
            outer_points.append((x, 2360))

    # filler gap
    for x in range(4350, 4590, 10):
        outer_points.append((x, 2360))

    # straight y section 9
    for y in range(2360, 3010, 10):
        if y <= 2600:
            outer_points.append((4590, y))
        else:
            outer_points.append((4590, y))
            inner_points.append((4350, y))

    # filler gap
    for y in range(3010, 3240, 10):
        outer_points.append((4590, y))

    # straight x section 6
    for x in range(4590, 3710, -10):
        if x >= 4350:
            outer_points.append((x, 3240))
        else:
            outer_points.append((x, 3240))
            inner_points.append((x, 3000))

    obstacle_points.append([])
    # obstacle 9
    for x in range(4100, 4010, -10):
        obstacle_points[8].append((x, 3090))
    for y in range(3090, 3160, 10):
        obstacle_points[8].append((4020, y))
    for x in range(4020, 4110, 10):
        obstacle_points[8].append((x, 3150))
    for y in range(3150, 3080, -10):
        obstacle_points[8].append((4110, y))

    # filler gap
    for x in range(3710, 3480, -10):
        inner_points.append((x, 3000))

    # straigt y section 10
    for y in range(3000, 3410, 10):
        if y <= 3240:
            inner_points.append((3480, y))
        else:
            inner_points.append((3480, y))
            outer_points.append((3720, y))

    # filler gap
    for y in range(3410, 3640, 10):
        outer_points.append((3720, y))

    # straight x section 7
    for x in range(3720, 3030, -10):
        if x >= 3480:
            outer_points.append((x, 3640))
        else:
            outer_points.append((x, 3640))
            inner_points.append((x, 3400))

    # filler gap
    for x in range(3030, 2800, -10):
        outer_points.append((x, 3640))

    # straight y section 11
    for y in range(3640, 3230, -10):
        if y >= 3400:
            outer_points.append((2800, y))
        else:
            outer_points.append((2800, y))
            inner_points.append((3040, y))

    # filler gap
    for y in range(3230, 3000, -10):
        inner_points.append((3040, y))

    # straight x section 8
    for x in range(3040, 2510, -10):
        if x >= 2800:
            inner_points.append((x, 3000))
        else:
            inner_points.append((x, 3000))
            outer_points.append((x, 3240))

    # filler gap
    for x in range(2510, 2280, -10):
        inner_points.append((x, 3000))

    # straigt y section 12
    for y in range(3000, 3410, 10):
        if y <= 3240:
            inner_points.append((2280, y))
        else:
            inner_points.append((2280, y))
            outer_points.append((2520, y))

    # filler gap
    for y in range(3410, 3640, 10):
        outer_points.append((2520, y))

    # straight x section 9
    for x in range(2520, 1830, -10):
        if x >= 2280:
            outer_points.append((x, 3640))
        else:
            outer_points.append((x, 3640))
            inner_points.append((x, 3400))

    # filler gap
    for x in range(1830, 1600, -10):
        outer_points.append((x, 3640))

    # straight y section 13
    for y in range(3640, 3230, -10):
        if y >= 3400:
            outer_points.append((1600, y))
        else:
            outer_points.append((1600, y))
            inner_points.append((1840, y))

    # filler gap
    for y in range(3230, 3000, -10):
        inner_points.append((1840, y))

    # straight x section 10
    for x in range(1840, 530, -10):
        if x >= 1600:
            inner_points.append((x, 3000))
        else:
            inner_points.append((x, 3000))
            outer_points.append((x, 3240))
    # filler gap
    for x in range(530, 280, -10):
        outer_points.append((x, 3240))

    # straight y section 14:
    for y in range(3240, 1010, -10):
        if y >= 3000:
            outer_points.append((280, y))
        else:
            outer_points.append((280, y))
            inner_points.append((520, y))

    obstacle_points.append([])
    # obstacle 10
    for x in range(80):
        obstacle_points[9].append(
            (math.cos(((x * math.pi) / 40)) * 30 + 400, math.sin(((x * math.pi) / 40)) * 30 + 2500))

    obstacle_points.append([])
    # obstacle 11
    for x in range(280, 340, 10):
        obstacle_points[10].append((x, 1700))
    for y in range(1700, 1630, -10):
        obstacle_points[10].append((330, y))
    for x in range(330, 270, -10):
        obstacle_points[10].append((x, 1640))

    obstacle_points.append([])
    # obstacle 12
    for x in range(520, 470, -10):
        obstacle_points[11].append((x, 1300))
    for y in range(1300, 1360, 10):
        obstacle_points[11].append((480, y))
    for x in range(480, 530, 10):
        obstacle_points[11].append((x, 1360))
    return {
        'outer': outer_points,
        'inner': inner_points,
        'obstacle': obstacle_points,
        'checkpoint': checkpoints,
        'finish': finish_line
    }


calculate_points = [
    map_1, map_2, map_3
]

class Map:
    def __init__(self, id, image, start_pos, npc_pos, player_pos, npc_dir, player_rotation, music, red_bias, blue_bias):
        self.id = id
        self.image = pygame.image.load(image) if image is not None else None
        self.start_pos=start_pos
        self.npc_pos=npc_pos

        self.outer_points = calculate_points[self.id]()['outer']
        self.inner_points = calculate_points[self.id]()['inner']
        #self.obstacle_points = calculate_points[self.id]()['obstacle']
        self.checkpoints = calculate_points[self.id]()['checkpoint']
        self.finish = calculate_points[self.id]()['finish']
        self.player_pos = player_pos
        self.player_rotation = player_rotation
        self.npc_dir = npc_dir
        self.music = music
        self.red_bias = red_bias
        self.blue_bias = blue_bias

        self.wall_segments = []
        for i in range(len(self.inner_points)):
            self.wall_segments.append((self.inner_points[i - 1], self.inner_points[i]))
        for i in range(len(self.outer_points)):
            self.wall_segments.append((self.outer_points[i - 1], self.outer_points[i]))
       # for i in self.obstacle_points:
            #for j in range(len(i)):
                #self.wall_segments.append((i[j - 1], i[j]))

        self.width = abs(max(point[0] for point in self.outer_points)) + abs(min(point[0] for point in self.outer_points))
        self.height = abs(max(point[1] for point in self.outer_points)) + abs(min(point[1] for point in self.outer_points))

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.outer_polygons_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.inner_polygons_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        pygame.draw.polygon(self.surface, (255, 255, 255), self.outer_points)
        pygame.draw.polygon(self.surface, (50, 50, 50), self.inner_points)

        pygame.draw.polygon(self.outer_polygons_surface, (255, 255, 255), self.outer_points)
        pygame.draw.polygon(self.inner_polygons_surface, (50, 50, 50), self.inner_points)

        self.outer_polygons_mask = pygame.mask.from_surface(self.outer_polygons_surface)
        self.inner_polygons_mask = pygame.mask.from_surface(self.inner_polygons_surface)

        pygame.transform.scale(self.surface, (self.width / camera.scale, self.height / camera.scale))


    def checker_count(self, npc_car):
        if (self.start_pos[2] <= npc_car.pos[0] <= (self.start_pos[2] + 20)) and (
                self.start_pos[3] <= npc_car.pos[1] <= (self.start_pos[3] + 240)):
            npc_car.checker=npc_car.laps
            print(npc_car.checker)

    def lap_checker(self, npc_car, total_laps):
        if (self.start_pos[0] <= npc_car.pos[0] < (self.start_pos[0] + 20)) and (
                self.start_pos[1] <= npc_car.pos[1] <= (self.start_pos[1] + 240)):
            npc_car.laps=npc_car.checker+1
            print(npc_car.laps)
        if npc_car.laps==total_laps+1:
            return True
        else:
            return False

maps = [
    Map(0, 'images/maps/map_2.png',[1790, 2600, 1900, 2600], [1850,2650], [80,1175], 180, (math.radians(180), 180), "assets/Map1_Music.mp3", "right", "left"),
    Map(1, 'images/maps/map_2.png',[3280, 110, 3000, 110],[3270, 180], [942, -1562], 0, (0,0), "assets/Map2_Music.mp3", "left", "right"),
    Map(2, 'images/maps/map_3.png', [1020, 3000, 1200, 3000], [1050, 3070], [-1382,1187], 180, (math.radians(180), 180), "assets/Map3_Music.mp3","right", "left"),
]
