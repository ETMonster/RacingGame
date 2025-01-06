import math

class trial_npc:
    def __init__ (self,image, pos, dir, speed, max_angle, bias, name,laps, checker):
        self.image=image
        self.pos = pos
        self.dir = dir
        self.speed = speed
        self.max_angle = max_angle
        self.rays=[]
        self.name=name
        self.laps=laps
        self.checker=checker
        for x in range(3):
            self.rays.append(Ray(self.pos,((x*60)-60),1000))
        self.bias = bias

    def update(self, wall_segments, inner_points, outer_points): #method for updating car's functions
        self.drive()
        self.update_rays(wall_segments)
        self.update_direction()
        self.collision_checker(inner_points, outer_points)


    def drive(self): #method that implements basic driving
        angle = self.dir * (math.pi / 180)
        self.pos[0]= self.pos[0] + (self.speed * math.cos(angle))
        self.pos[1]= self.pos[1] + (self.speed * math.sin(angle))


    def update_rays(self,wall_segments): #method that calls the ray's update methods
        for x in self.rays:
            x.update(self.pos, self.dir, wall_segments)

    def update_direction(self): #method that is used to change the car's direction
        longest_ray_distance, index=0, 0
        ray_index=0

        #change right ray distance so that the car is offset from center to the right
        if self.bias == "right":
            if self.rays[0].distance>=150:
                self.rays[2].distance=self.rays[2].distance+150
        #do the same for left ray
        elif self.bias == "left":
            if self.rays[2].distance>=150:
                self.rays[0].distance=self.rays[0].distance+150
        #loop to find the longest ray/direction with most room to move

        for x in self.rays:
            if x.distance>=longest_ray_distance:
                longest_ray_distance=x.distance
                ray_index=index
            index=index+1

        #next we change the direction based on the longest ray
        if ray_index==0: #this will be the ray coming from the left of the car
            self.dir=self.dir-self.max_angle
        elif ray_index==1: #since the forward ray will most likely be the longest ray the most often, to introduce more turning, we will take into account the other two rays and send the car in an average direction
            if self.rays[0].distance>self.rays[2].distance: #if the left ray is longer, then we send the car half the max_angle
                self.dir=self.dir-(self.max_angle/2)
            elif self.rays[0].distance<self.rays[2].distance: #we do the same for the right side but opposite
                self.dir=self.dir+(self.max_angle/2)
        elif ray_index==2:
            self.dir=self.dir+self.max_angle

    #program should theoretically work without this
    def collision_checker(self, inner_points, outer_points):
        if (self.pos[0] and self.pos[1] in inner_points) or (self.pos[0] and self.pos[1] in outer_points):
            angle = self.dir * (math.pi / 180)
            self.pos[0] = self.pos[0] - (self.speed * math.cos(angle))
            self.pos[1] = self.pos[1] - (self.speed * math.sin(angle))




class Ray:
    def __init__(self, pos, angle1,length):
        self.pos1 = pos
        self.angle1=angle1
        self.length = length
        self.dir1=None
        self.distance=self.length

    def update(self, pos, dir, wall_segments):
        #update method
        self.pos1=pos #starting point of ray is the same as that of the car
        self.update_direction(dir) #calls two other methods
        self.update_intersection(wall_segments)

    def update_direction(self, dir): #method to update direction of ray
        #temp angle is used to so that the angle of the ray stays consistent even when the car turns. Dir is the car's direction
        temp_angle=self.angle1+dir
        rad_angle=temp_angle*(math.pi/180)

        self.dir1=(math.cos(rad_angle), math.sin(rad_angle))

    def update_intersection(self, wall_segments): #method to update the intersection of the rays with wall segments

        distance=self.length #set distance to length
        for x in wall_segments:
            x1=x[0][0] #x and y coordinate for one side of wall segment
            y1=x[0][1]
            x2=x[1][0] #x and y coordinate for other side of wall segment
            y2=x[1][1]
            x3=self.pos1[0] #x and y coordinate for starting point of ray
            y3=self.pos1[1]
            x4=self.pos1[0]+self.dir1[0]*self.length #x and y coordinate for ending point of ray
            y4=self.pos1[1]+self.dir1[1]*self.length

            #use line-line intersection formula to calculate intersection of two line segments
            denominator= (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
            if denominator==0: #if the denominator is 0, that means the segments are parallel or coincide
                continue
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

            #if 0<=t<=1 then the lines intersect at x=(x1+t(x2-x1) and y=(y1+t(y2-y1)). The same can be said for u but we only need one of u or t
            if t >= 0 and t <= 1 and u > 0:
                x_intersection=x1+t*(x2-x1)
                y_intersection=y1+t*(y2-y1)
                temp_distance = ((self.pos1[0]-x_intersection)**2+(self.pos1[1]-y_intersection)**2)**0.5 #calculate distance from starting point of ray to intersection
                if temp_distance<distance: #replace distance with temp_distance if temp_distance is smaller
                    distance=temp_distance

        #once loop is over set new value
        self.distance=distance






