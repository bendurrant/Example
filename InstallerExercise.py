import sys
import math


class Node(object):
    def __init__(self,package):
        self.package = package
        self.visited = False
        self.previous = None
        self.childPackages = [] #all packages that depend on self.package
        self.preTime = 0
        self.postTime = 0
    def addNewChildPackage(self,packageName):
        self.childPackages.append(packageName)

    #this one is a little tricky to read on its own. I want two of these to be
    #equivilant iff the packages are the same and the list of all the packages
    #that depend on this package are the same
    def __eq__(self,another):
        return (hasattr(another, "package") and self.package == another.package
                and sorted(self.childPackages) == sorted(another.childPackages))
    def __hash__(self):
        return hash(self.package)
    def __str__(self):
        return self.package
    def __repr__(self):
        return self.package
    
def InstallerExercise(inputArray):
    graph = createGraph(inputArray)
    topSortOutput = []
    dfs(graph,topSortOutput)
    topSortOutput.reverse()
    outputString = ", ".join(topSortOutput)
    print(outputString)
    return outputString
    
def createGraph(inputArray):
    graph= {}
    
    for i in inputArray:
        package,dependsOn = i.split(": ")
        if(len(dependsOn) > 0):
            if(dependsOn in graph):
                graph[dependsOn].addNewChildPackage(package)
            else:
                parentNode = Node(dependsOn)
                parentNode.addNewChildPackage(package)
                graph[dependsOn] = parentNode
        if(package not in graph):
            node = Node(package)
            graph[package] = node
            
    return graph

def dfs(graph, topSort):
    clock = 1
    for package in graph:
        graph[package].visited = False
    for package in graph:
        if not graph[package].visited:           
            clock = explore(graph,package,clock,topSort)


def explore(graph, package,clock,topSort):
    graph[package].visited = True
    graph[package].preTime = clock
    clock+=1
    for child in graph[package].childPackages:
        #this if statement finds the circular dependency.
        if (graph[child].preTime >0 and graph[child].postTime <1):
            raise(ValueError("Circular Dependency found"))
        if not (graph[child].visited):
            clock = explore(graph,child,clock,topSort)
    graph[package].postTime = clock
    clock +=1
    topSort.append(package)
    return clock
    
