import unittest
from InstallerExercise import InstallerExercise

class InstallerExerciseTestMethods(unittest.TestCase):

    def testExpectedStringParse(self):
        testArray = ["French Fries: Potatos","Bacon: Pigs"]
        testArrayASGraph= {};
        testArrayASGraph["French Fries"] = "Potato"
        testArrayASGraph["Bacon"] = "Pigs"
        self.assertEqual(testArrayASGraph, InstallerExercise(["French Fries: Potatos","Bacon: Pigs"]))
        
    

if __name__=='__main__':
    unittest.main()
