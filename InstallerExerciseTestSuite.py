import unittest
from InstallerExercise import createGraph
from InstallerExercise import InstallerExercise
from InstallerExercise import Node
from InstallerExercise import dfs

class InstallerExerciseTestMethods(unittest.TestCase):
    maxDiff = None
    def testExpectedStringParse(self):
        testArray = ["French Fries: Potatos","Pigs: ","Potatos: ","Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["French Fries"] = Node("French Fries")
        testArrayASGraph["Pigs"] = Node("Pigs")
        testArrayASGraph["Bacon"] = Node("Bacon")
        testArrayASGraph["Potatos"] = Node("Potatos")


        testArrayASGraph["Bacon"].addDependency("Pigs")
        testArrayASGraph["French Fries"].addDependency("Potatos")
        self.assertDictEqual(testArrayASGraph, createGraph(testArray))
        
    def testSingleElementInGraph(self):
        testArray = ["Bacon: Pigs", "Pigs: "]
        testArrayASGraph= {};
        testArrayASGraph["Bacon"] = Node("Bacon")
        testArrayASGraph["Pigs"] = Node("Pigs")

        testArrayASGraph["Bacon"].addDependency("Pigs")
        
        self.assertDictEqual(testArrayASGraph, createGraph(testArray))
       
    def testLargeNumOfElementInGraph(self):
        testArray = ["French Fries: Potatos","Potatos: ","Pigs: ","Bacon: Pigs","KittenService: ",
                     "Leetmeme: Cyberportal","Cyberportal: Ice","CamelCaser: KittenService",
                     "Fraudstream: Leetmeme","Ice: "]

        #set up initial nodes
        testArrayASGraph= {}
        testArrayASGraph["French Fries"] = Node("French Fries")
        testArrayASGraph["Potatos"] = Node("Potatos")
        testArrayASGraph["Pigs"] = Node("Pigs")
        testArrayASGraph["Bacon"] = Node("Bacon")
        testArrayASGraph["KittenService"] = Node("KittenService")
        testArrayASGraph["Leetmeme"] = Node("Leetmeme")
        testArrayASGraph["Cyberportal"] = Node("Cyberportal")
        testArrayASGraph["CamelCaser"] = Node("CamelCaser")
        testArrayASGraph["Fraudstream"] = Node("Fraudstream")
        testArrayASGraph["Ice"] = Node("Ice")

        #put in dependencies
        testArrayASGraph["Bacon"].addDependency("Pigs")
        testArrayASGraph["French Fries"].addDependency("Potatos")
        
        testArrayASGraph["Leetmeme"].addDependency("Cyberportal")
        testArrayASGraph["Cyberportal"].addDependency("Ice")
        testArrayASGraph["CamelCaser"].addDependency("KittenService")
        testArrayASGraph["Fraudstream"].addDependency("Leetmeme")


        
        self.assertDictEqual(testArrayASGraph, createGraph(testArray))


    def testDfsFindsCycle(self):
        with self.assertRaises(ValueError):
            InstallerExercise(["Leetmeme: Cyberportal","Cyberportal: Ice","Ice: Leetmeme"])
    def testExpectedOutput(self):
        testArray = ["KittenService: ","Leetmeme: Cyberportal","Cyberportal: Ice",
                           "CamelCaser: KittenService","Fraudstream: Leetmeme","Ice: "]

        self.assertEqual("KittenService, Ice, Cyberportal, Leetmeme, CamelCaser, Fraudstream",
                          InstallerExercise(testArray))

    def testNoDependency(self):
        testArray = ["Potato: ", "Bacon: ", "Broccoli: "]
        self.assertEqual("Potato, Bacon, Broccoli", InstallerExercise(testArray))

    
        

if __name__=='__main__':
    unittest.main()
