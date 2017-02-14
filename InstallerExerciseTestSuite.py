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


        testArrayASGraph["Pigs"].addNewChildPackage("Bacon")
        testArrayASGraph["Potatos"].addNewChildPackage("French Fries")
        #print(testArrayASGraph["Pigs"].childPackages)
        self.assertDictEqual(testArrayASGraph, createGraph(testArray))
        
    def testSingleElementInGraph(self):
        testArray = ["Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["Bacon"] = Node("Bacon")
        testArrayASGraph["Pigs"] = Node("Pigs")

        testArrayASGraph["Pigs"].addNewChildPackage("Bacon")
        
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
        testArrayASGraph["Potatos"].addNewChildPackage("French Fries")
        testArrayASGraph["Pigs"].addNewChildPackage("Bacon")
        testArrayASGraph["Cyberportal"].addNewChildPackage("Leetmeme")
        testArrayASGraph["Ice"].addNewChildPackage("Cyberportal")
        testArrayASGraph["KittenService"].addNewChildPackage("CamelCaser")
        testArrayASGraph["Leetmeme"].addNewChildPackage("Fraudstream")


        
        self.assertDictEqual(testArrayASGraph, createGraph(testArray))


    def testDfsFindsCycle(self):
        with self.assertRaises(ValueError):
            InstallerExercise(["Leetmeme: Cyberportal","Cyberportal: Ice","Ice: Leetmeme"])
    def testExpectedOutput(self):
        testArray = ["KittenService: ","Leetmeme: Cyberportal","Cyberportal: Ice",
                           "CamelCaser: KittenService","Fraudstream: Leetmeme","Ice: "]

        self.assertEqual("Ice, Cyberportal, Leetmeme, Fraudstream, KittenService, CamelCaser",
                          InstallerExercise(testArray))

    def testNoDependency(self):
        testArray = ["Potato: ", "Bacon: ", "Broccoli: "]
        self.assertEqual("Broccoli, Bacon, Potato", InstallerExercise(testArray))

    
        

if __name__=='__main__':
    unittest.main()
