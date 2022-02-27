import math
import numpy as np
class myConvexHull:
    points = []
    outermostPointIndex = []
    simplices = []
    def __init__(self, paramPoints):
        self.myConvexHull(paramPoints)
    def myConvexHull(self, paramPoints):
        self.simplices = []
        self.points = paramPoints
        #just a list of indexes
        pointIndex = [i for i in range(len(self.points))]

        #find the leftmost and rightmost point and append them to an array
        self.outermostPointIndex = []
        leftmostidx = 0
        rightmostidx = 0
        for i in range(len(self.points)):
            if(self.points[i][0] <  self.points[leftmostidx][0]):
                leftmostidx = i
            if(self.points[i][0] >  self.points[rightmostidx][0]):
                rightmostidx = i
        self.outermostPointIndex.append(leftmostidx)
        self.outermostPointIndex.append(rightmostidx)

        #split points into two section
        x1 = self.points[leftmostidx][0]
        y1 = self.points[leftmostidx][1]
        x2 = self.points[rightmostidx][0]
        y2 = self.points[rightmostidx][1]
        upperSection = self.GetPointsInSection(pointIndex, x1, y1, x2, y2, "up")
        lowerSection = self.GetPointsInSection(pointIndex, x1, y1, x2, y2, "down")

        #answer is outermost points from left section and right section
        self.FindOuterIndex(upperSection, leftmostidx, rightmostidx, "up")
        self.FindOuterIndex(lowerSection, leftmostidx, rightmostidx, "down")
        #print(self.points[self.outermostPointIndex])
        #print(self.outermostPointIndex)
        self.simplices = np.array(self.simplices)
    def GetPointsInSection(self, pointIndex, x1, y1, x2, y2, section): #returns index of points in desired section
        upperSection = []
        lowerSection = []
        for i in pointIndex:
            x3 = self.points[i][0]
            y3 = self.points[i][1]
            if (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3) > 0 and not (x3 == x1 and y3 == y1) and not (x3 == x2 and y3 == y2):
                upperSection.append(i)
            elif (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3) < 0 and not (x3 == x1 and y3 == y1) and not (x3 == x2 and y3 == y2):
                lowerSection.append(i)
        if section == "up":
            return upperSection
        else:
            return lowerSection

    def FindOuterIndex(self, pointIndex, idx1, idx2, direction): #adds outermost points
        p1 = self.points[idx1]
        p2 = self.points[idx2]
        
        if pointIndex != []: #recurrence
            farthestPoint = self.GetFarthestPoint(pointIndex, p1, p2)
            if farthestPoint >=0:
                self.outermostPointIndex.append(farthestPoint)
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            xMax = self.points[farthestPoint][0]
            yMax = self.points[farthestPoint][1]
            s1 = self.GetPointsInSection(pointIndex, x1, y1, xMax, yMax, direction)
            s2 = self.GetPointsInSection(pointIndex, xMax, yMax, x2, y2, direction)
            self.FindOuterIndex(s1, idx1, farthestPoint, direction)
            self.FindOuterIndex(s2, farthestPoint, idx2, direction)
        else: #base : if pointIndex is empty then append idx1 and idx2
            if [idx1, idx2] not in self.simplices and idx1 != -1 and idx2 != -1:
                self.simplices.append([idx1, idx2])

    def GetFarthestPoint(self, pointIndex, p1, p2): #returns the index of the farthest point in points from line p1p2
        #finding the linear equation that satisfies p1 and p2: Ax + By + C = 0
        #using the formula (y1 – y2)x + (x2 – x1)y + (x1y2 – x2y1) = 0
        A = p1[1] - p2[1]
        B = p2[0] - p1[0]
        C = p1[0]*p2[1] - p2[0]*p1[1]
        maximum = 0
        maxidx = -1
        for i in pointIndex:
            distance = abs(A*self.points[i][0] + B*self.points[i][1] + C)/math.sqrt(A*A + B*B)
            if (distance > maximum):
                maximum = distance
                maxidx = i
        return maxidx