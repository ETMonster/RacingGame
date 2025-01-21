import pygame
from constants import *

def map_1():
    inner_points, outer_points, obstacle_points = [], [], []

    for y in range(2830, 2600, -10):
        outer_points.append((280, y))

    obstacle_points.append([])
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
    inner_points += (ellipse_points(center, x1, y1, -1, 0))

    # curve 1 outer (larger ellipse) h
    center = [1000, 600]
    x1 = 720
    y1 = 360
    outer_points += (ellipse_points(center, x1, y1, -1, 0))

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
    outer_points += (ellipse_points(center, x1, y1, 1, 0, rotated=True))
    # curve 2 inner (larger ellipse) v
    center = [1100, 1590]
    x1 = 440
    y1 = 590
    inner_points += (ellipse_points(center, x1, y1, 1, 0, rotated=True))

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
    outer_points += (ellipse_points(center, x1, y1, -1, 0, rotated=True))

    # curve 3 inner (smaller ellipse) v
    center = [2700, 1450]
    x1 = 110
    y1 = 250
    inner_points += (ellipse_points(center, x1, y1, -1, 0, rotated=True))

    # straight x section 4
    for x in range(2700, 2640, -10):
        outer_points.append((x, 1940))
        inner_points.append((x, 1700))

    # curve 4 outer (smaller ellipse) v
    center = [2650, 2140]
    x1 = 110
    y1 = 200
    outer_points += (ellipse_points(center, x1, y1, 1, 0, rotated=True))

    # curve 4 inner (bigger ellipse) v
    center = [2650, 2140]
    x1 = 350
    y1 = 440
    inner_points += (ellipse_points(center, x1, y1, 1, 0, rotated=True))

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
        'inner': inner_points
    }
def map_2():
    inner_points, outer_points, obstacle_points, checkpoints = [], [], [], []

    checkpoints.append(pygame.Rect(3900, 3190, 30, 240))
    checkpoints.append(pygame.Rect(550, 2600, 240, 30))
    checkpoints.append(pygame.Rect(1480, 800, 240, 30))
    checkpoints.append(pygame.Rect(2100, 800, 30, 240))

    # end of straight
    for y in range(840, 590, -10):
        outer_points.append((280, y))
        inner_points.append((520, y))

    # curve 1 outer h
    center = [1000, 600]
    x1 = 720
    y1 = 360
    outer_points += (ellipse_points(center, x1, y1, -1, 0))

    # curve 1 inner h
    center = [1000, 600]
    x1 = 480
    y1 = 120
    inner_points += (ellipse_points(center, x1, y1, -1, 0))

    # straight y section 1
    for y in range(600, 1510, 10):
        outer_points.append((1720, y))
        inner_points.append((1480, y))

    # curve 2 outer h
    center = [1930, 1500]
    x1 = 210
    y1 = 110
    outer_points += (ellipse_points(center, x1, y1, 1, 0))

    # curve 2 inner h
    center = [1930, 1500]
    x1 = 450
    y1 = 350
    inner_points += (ellipse_points(center, x1, y1, 1, 0))

    # curve 3 inner h
    center = [2590, 1500]
    x1 = 210
    y1 = 110
    inner_points += (ellipse_points(center, x1, y1, -1, 0))

    # curve 3 outer h
    center = [2590, 1500]
    x1 = 450
    y1 = 350
    outer_points += (ellipse_points(center, x1, y1, -1, 0))

    # curve 4 outer h
    center = [3250, 1500]
    x1 = 210
    y1 = 110
    outer_points += (ellipse_points(center, x1, y1, 1, 0))

    # curve 4 inner h
    center = [3250, 1500]
    x1 = 450
    y1 = 350
    inner_points += (ellipse_points(center, x1, y1, 1, 0))

    # straight y section 2
    for y in range(1500, 690, -10):
        outer_points.append((3460, y))
        inner_points.append((3700, y))

    # curve 5 outer h
    center = [3360, 700]
    x1 = 100
    y1 = 60
    outer_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 5 inner h
    center = [3360, 700]
    x1 = 340
    y1 = 300
    inner_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 6 inner h
    center = [2920, 700]
    x1 = 100
    y1 = 60
    inner_points += (ellipse_points(center, x1, y1, 1, 1))

    # curve 6 outer h
    center = [2920, 700]
    x1 = 340
    y1 = 300
    outer_points += (ellipse_points(center, x1, y1, 1, 1))

    # curve 7 outer h
    center = [2480, 700]
    x1 = 100
    y1 = 60
    outer_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 7 inner h
    center = [2480, 700]
    x1 = 340
    y1 = 300
    inner_points += (ellipse_points(center, x1, y1, -1, 1))

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
    inner_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 8 outer v
    center = [4100, 450]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 9 outer v
    center = [4100, 890]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 9 inner v
    center = [4100, 890]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 10 inner v
    center = [4100, 1330]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 10 outer v
    center = [4100, 1330]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 11 outer v
    center = [4100, 1770]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 11 inner v
    center = [4100, 1770]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 12 inner v
    center = [4100, 2210]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 12 outer v
    center = [4100, 2210]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 13 outer v
    center = [4100, 2650]
    y1 = 100
    x1 = 60
    outer_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 13 inner v
    center = [4100, 2650]
    y1 = 340
    x1 = 300
    inner_points += (ellipse_points(center, x1, y1, 1, 0, rotated = True))

    # curve 14 inner v
    center = [4100, 3090]
    y1 = 100
    x1 = 60
    inner_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

    # curve 14 outer v
    center = [4100, 3090]
    y1 = 340
    x1 = 300
    outer_points += (ellipse_points(center, x1, y1, -1, 0, rotated = True))

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
    outer_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 15 inner h
    center = [3260, 2800]
    x1 = 490
    y1 = 390
    inner_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 16 inner h
    center = [2520, 2800]
    x1 = 250
    y1 = 150
    inner_points += (ellipse_points(center, x1, y1, 1, 1))

    # curve 16 outer h
    center = [2520, 2800]
    x1 = 490
    y1 = 390
    outer_points += (ellipse_points(center, x1, y1, 1, 1))

    # curve 17 outer h
    center = [1780, 2800]
    x1 = 250
    y1 = 150
    outer_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 17 inner h
    center = [1780, 2800]
    x1 = 490
    y1 = 390
    inner_points += (ellipse_points(center, x1, y1, -1, 1))

    # curve 18 inner h
    center = [1040, 2800]
    x1 = 250
    y1 = 150
    inner_points += (ellipse_points(center, x1, y1, 1, 1))

    # curve 18 outer h
    center = [1040, 2800]
    x1 = 490
    y1 = 390
    outer_points += (ellipse_points(center, x1, y1, 1, 1))

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
    }

calculate_points = [
    map_1, map_2
]

class Map:
    def __init__(self, id, image = None):
        self.id = id
        self.image = pygame.image.load(image) if image is not None else None

        self.outer_points = calculate_points[self.id]()['outer']
        self.inner_points = calculate_points[self.id]()['inner']

        self.width = abs(max(point[0] for point in self.outer_points)) + abs(min(point[0] for point in self.outer_points))
        self.height = abs(max(point[1] for point in self.outer_points)) + abs(min(point[1] for point in self.outer_points))

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        pygame.draw.polygon(self.surface, (255, 255, 255), self.outer_points)
        pygame.draw.polygon(self.surface, (50, 50, 50), self.inner_points)

        pygame.transform.scale(self.surface, (self.width / camera.scale, self.height / camera.scale))

maps = [
    Map(0),
    Map(1, 'images/maps/map_2.png'),
]