import unittest
from InstallerExercise import InstallerExercise

class InstallerExerciseTestMethods(unittest.TestCase):

    def testExpectedStringParse(self):
        testArray = ["French Fries: Potatos","Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["French Fries"] = "Potato"
        testArrayASGraph["Bacon"] = "Pigs"
        self.assertEqual(testArrayASGraph, InstallerExercise(testArray))
        
    def testSingleElementInGraph(self):
        testArray = ["Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["Bacon"] = "Pigs"
        self.assertEqual(testArrayASGraph, InstallerExercise(testArray))
    def testLargeNumOfElementInGraph(self):
        testArray = ["French Fries: Potatos","Bacon: Pigs","KittenService: CamelCaser",
                     "Leetmeme: Cyberportal","Cyberportal: Ice","CamelCaser: KittenService",
                     "Fraudstream: Leetmeme","Ice: "]
        testArrayASGraph= {}
        testArrayASGraph["French Fries"] = "Potato"
        testArrayASGraph["Bacon"] = "Pigs"
        testArrayASGraph["KittenService"] = None
        testArrayASGraph["Leetmeme"] = "Cyberportal"
        testArrayASGraph["Cyberportal"] = "Ice"
        testArrayASGraph["CamelCaser"] = "KittenService"
        testArrayASGraph["Fraudstream"] = "Leetmeme"
        testArrayASGraph["Ice"] = None
        self.assertEqual(testArrayASGraph, InstallerExercise(testArray))

if __name__=='__main__':
    unittest.main()
