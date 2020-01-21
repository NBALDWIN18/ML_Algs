'''
Author: NBALDWIN18
Description: Implements K-nearest neighbor
algorithm without the use of any libraries
'''

class KNN():
    
    #A structure to represent labeled data points
    class Point():

        '''
        Initializaes a point
        :param loc: a list representing the coordinates for the point
        :param label: the label or class for the point
        '''
        def __init__(self, loc, label):
            self.location = loc
            self.label = label

    '''
    Initializes a KNN model
    :param k: the k value
    :param data: list of data tuples (coordinates, label)
    '''
    def __init__(self, k, data):
        self.k = k
        self.points = []
        for point in data:
            self.points.append(self.Point(point[0], point[1]))

    '''
    Finds the distance between a point and a location
    :param p1: a point
    :param loc: a list of coordinates
    :return: the distance between the locations
    '''
    def distance(self, p1, loc):
        sum = 0
        for x,y in zip(p1.location, loc):
            sum += (x - y)**2
        return (sum **0.5)

    '''
    Predicts the label at the location
    :param location: a list of coordinates
    :return: the predicted label
    '''
    def predict(self,location):
        distances = []
        for point in self.points:
            distances.append((self.distance(point, location), point.label))
            distances = sorted(distances)[:self.k]
            d, labels = list(zip(*distances))
        return max(set(labels), key = labels.count)