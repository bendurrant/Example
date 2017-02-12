import sys
import math


class Node(object):
    def __init__(self,package,dependency):
        self.package = package
        self.visited = False
        self.previous = None
        self.depend = dependency
        self.preTime = 0
        self.postTime = 0
    def __eq__(self,another):
        return hasattr(another, "package") and self.package == another.package
    def __hash__(self):
        return hash(self.package)
    
def InstallerExercise(inputArray):
    graph = createGraph(inputArray)
    return graph
    
def createGraph(inputArray):
    graph= {}
    nodes = {}
    tempStringHolder = []
    for i in inputArray:
        tempStringHolder = i.split(": ")
        print(tempStringHolder)
        if(len(tempStringHolder[1]) == 0):
            dependency = None
        else:
            dependency = tempStringHolder[1]
        node = Node(tempStringHolder[0],dependency)
        graph[node.package] = node
    return graph
