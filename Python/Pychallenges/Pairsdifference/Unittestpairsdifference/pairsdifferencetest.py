import unittest
from ChallengeModule.pairsdifference import searchbinary
from ChallengeModule.pairsdifference import pairs

class MyTestPairdifference(unittest.TestCase):
    def setUp(self):
        #make sure the input array is SORTED
        print("Initializing test data")
        self.case1 = [[],0,0,0]
        self.case2 = [[1,2,3,4],5, 0, 4]
        self.case3 = [[1,2,3,4],3, 0, 4]
        self.case4 = [[1,2,3,4,5],2, 0, 5]
        self.case5 = [[1,2,4,7,13],4, 0, 5]


    def test_searchbinary(self):
        case_1 = self.case1
        mycase1_ret = searchbinary(case_1[1],case_1[2],case_1[3],case_1[0])
        self.assertEqual(0, mycase1_ret,"Should be 0")
        print("Case 1 is OK")

        case_2 = self.case2
        mycase2_ret = searchbinary(case_2[1], case_2[2], case_2[3], case_2[0])
        self.assertEqual(0, mycase2_ret, "Should be 0")
        print("Case 2 is OK")

        case_3 = self.case3
        mycase3_ret = searchbinary(case_3[1], case_3[2], case_3[3], case_3[0])
        self.assertEqual(1, mycase3_ret, "Should be 1")
        print("Case 3 is OK")

        case_4 = self.case4
        mycase4_ret = searchbinary(case_4[1], case_4[2], case_4[3], case_4[0])
        self.assertEqual(1, mycase4_ret, "Should be 1")
        print("Case 4 is OK")

        case_5 = self.case5
        mycase5_ret = searchbinary(case_5[1], case_5[2], case_5[3], case_5[0])
        self.assertEqual(1, mycase5_ret, "Should be 1")
        print("Case 5 is OK")


    def test_pairs(self):
        print("FUNCTION  TEST_PAIRS : ")
        case_1 = self.case1
        mycase1_ret = pairs(case_1[1], case_1[0])
        self.assertEqual(0, mycase1_ret, "Should be 0 because list is empty")
        print("Case 1 is OK")

        case_3 = self.case3
        mycase3_ret = pairs(case_3[1], case_3[0])
        self.assertEqual(1, mycase3_ret, "Should be 1")
        print("Case 3 is OK")

        case_4 = self.case4
        mycase4_ret = pairs(case_4[1], case_4[0])
        self.assertEqual(3, mycase4_ret, "Should be 3")
        print("Case 4 is OK")

        case_5 = self.case5
        mycase5_ret = pairs(case_5[1], case_5[0])
        self.assertEqual(0, mycase5_ret, "Should be 0 no pairs with difference 4")
        print("Case 5 is OK")




if __name__ == '__main__':
    unittest.main()
