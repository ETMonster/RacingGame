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

calculate_points = [
    map_1
]

class Map:
    def __init__(self, id, image):
        self.id = id
        self.image = image

        self.outer_points = calculate_points[self.id]()['outer']
        self.inner_points = calculate_points[self.id]()['inner']

maps = [
    Map(0, 'images/maps/map_1')
]