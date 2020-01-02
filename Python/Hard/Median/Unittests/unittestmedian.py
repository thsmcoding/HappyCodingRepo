import unittest
from Solutions.Median import partitionarray
from Solutions.Median import computemediantwoarrays
from Solutions.Median import mergesortedarrays
from Solutions.Median import findKelement


class MyMediansolution(unittest.TestCase):

    def setUp(self):
        print("Setting up all the necessary inputs")
        self.result= []
        self.list1 = []
        self.list2 = [1, 2, 3]
        self.list3 = [-1, 4, 5, 8, 9, 62]
        self.list4 = [1, 2]
        self.list5 = [-4, 5, 8, 9, 62]


    def test_mergesortedarrays(self):
        mergesortedarrays(self.list4, self.list5, self.result)
        expected = [-4,1,2,5,8,9,62]
        self.assertEqual(expected, self.result)
        print("Test merge two sorted arrays is OK")


    def test_findKthelement(self):
        expected_1 = None
        expected_2 = 8
        self.assertEqual(expected_2, findKelement(4,self.list3,[]))
        self.assertEqual(expected_1, findKelement(1,self.list1,[]))
        print("Test test_findKthelement is OK")


    def test_partitionarray(self):
        res_1 = partitionarray(self.list1, 3)
        res_2 = partitionarray(self.list2, 3)
        res_3 = partitionarray(self.list3, 3)
        self.assertEqual(0, len(res_1))
        self.assertEqual(3, len(res_2))
        self.assertEqual(4, len(res_3))
        print("Test partitionarray is OK")




if __name__ == '__main__':
    unittest.main()
