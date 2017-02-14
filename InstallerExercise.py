import sys
import math


class Node(object):
    def __init__(self,package):
        self.package = package
        self.visited = False
        self.dependsOn = None
        self.preTime = 0
        self.postTime = 0
    def addDependency(self,packageName):
        self.dependsOn = packageName

    def hasDependency(self):
        if(self.dependsOn is not None):
            return True
        else:
            return False

    #this one is a little tricky to read on its own. I want two of these to be
    #equivilant iff the packages are the same and the list of all the packages
    #that depend on this package are the same
    def __eq__(self,another):
        return (hasattr(another, "package") and self.package == another.package
                and self.dependsOn == another.dependsOn)
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
    outputString = ", ".join(topSortOutput)
    print(outputString)
    return outputString
    
def createGraph(inputArray):
    graph= {}   
    for i in inputArray:
        package,dependsOn = i.split(": ")
        if(package not in graph):
            node = Node(package)
            if(len(dependsOn)>0):
                node.addDependency(dependsOn)
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
    if(graph[package].hasDependency()):
        dependency = graph[package].dependsOn
        #this if statement finds the circular dependency.
        if (graph[dependency].preTime >0 and graph[dependency].postTime <1):
            raise(ValueError("Circular Dependency found"))
        if not (graph[dependency].visited):
            clock = explore(graph,dependency,clock,topSort)
    graph[package].postTime = clock
    clock +=1
    topSort.append(package)
    return clock
    
