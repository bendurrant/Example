import unittest
from InstallerExercise import InstallerExercise
from InstallerExercise import Node

class InstallerExerciseTestMethods(unittest.TestCase):
    maxDiff = None
    def testExpectedStringParse(self):
        testArray = ["French Fries: Potatos","Bacon: "]
        testArrayASGraph= {};
        testArrayASGraph["French Fries"] = Node("French Fries", "Potatos")
        testArrayASGraph["Bacon"] = Node("Bacon",None)
        self.assertDictEqual(testArrayASGraph, InstallerExercise(testArray))
        
    def testSingleElementInGraph(self):
        testArray = ["Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["Bacon"] = Node("Bacon","Pigs")
        self.assertDictEqual(testArrayASGraph, InstallerExercise(testArray))
       
    def testLargeNumOfElementInGraph(self):
        testArray = ["French Fries: Potatos","Bacon: Pigs","KittenService: ",
                     "Leetmeme: Cyberportal","Cyberportal: Ice","CamelCaser: KittenService",
                     "Fraudstream: Leetmeme","Ice: "]
        testArrayASGraph= {}
        testArrayASGraph["French Fries"] = Node("French Fries", "Potatos")
        testArrayASGraph["Bacon"] = Node("Bacon","Pigs")
        testArrayASGraph["KittenService"] = Node("KittenService",None)
        testArrayASGraph["Leetmeme"] = Node("Leetmeme","Cyberportal")
        testArrayASGraph["Cyberportal"] = Node("Cyberportal","Ice")
        testArrayASGraph["CamelCaser"] = Node("CamelCaser","KittenService")
        testArrayASGraph["Fraudstream"] = Node("Fraudstream","Leetmeme")
        testArrayASGraph["Ice"] = Node("Ice",None)
        self.assertDictEqual(testArrayASGraph, InstallerExercise(testArray))

if __name__=='__main__':
    unittest.main()
