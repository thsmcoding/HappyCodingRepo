import unittest
from Solution.BSTPackage.BinaryTreeNode import BinaryTreeNode
from Solution.BSTPackage.BSTModulefunctions import isaleaf
from Solution.BSTPackage.BSTModulefunctions import secondLargest
from Solution.BSTPackage.BSTModulefunctions import secondLargestValue
from Solution.BSTPackage.BSTModulefunctions import assignnewValue
from Solution.BSTPackage.BSTModulefunctions import maximum_tree
from Solution.BSTPackage.BSTModulefunctions import minimum_tree
from Solution.BSTPackage.BSTModulefunctions import secondSmallestValue


class MyTestBstclass(unittest.TestCase):
    def setUp(self):
        self.maximum_node = None
        self.minimum_node = None
        self.maximum__second_node = None
        self.minimum__second_node = None

        self.tree1 = None
        self.tree2 = BinaryTreeNode(50)

        self.tree3 = BinaryTreeNode(100)
        self.tree3.left = None
        self.tree3.right = BinaryTreeNode(200)

        self.tree4 = BinaryTreeNode(25)
        self.tree4.left = BinaryTreeNode(20)
        self.tree4.right = None

        self.tree5 = BinaryTreeNode(53)
        self.tree5.left = BinaryTreeNode(28)
        self.tree5.right = BinaryTreeNode(70)

        self.tree6 = BinaryTreeNode(11)
        self.tree6.left = BinaryTreeNode(9)
        self.tree6.left.left = BinaryTreeNode(7)
        self.tree6.left.right = BinaryTreeNode(10)
        self.tree6.right = BinaryTreeNode(55)
        self.tree6.right.right = BinaryTreeNode(60)
        self.tree6.right.left = BinaryTreeNode(48)

        self.tree7 = BinaryTreeNode(11)
        self.tree7.left = BinaryTreeNode(9)
        self.tree7.left.left = BinaryTreeNode(7)
        self.tree7.left.right = BinaryTreeNode(10)

        self.tree8 = BinaryTreeNode(11)
        self.tree8.left = BinaryTreeNode(10)
        self.tree8.right = BinaryTreeNode(55)
        self.tree8.right.left = BinaryTreeNode(48)


    def tearDown(self):
        print("Cleaning up two nodes after each test")
        self.maximum_node = None
        self.maximum__second_node = None
        self.minimum_node = None
        self.minimum__second_node = None



    def test_assignNewValue(self):
        self.assertEqual(None, assignnewValue(self.tree1,None))
        self.assertEqual(None, assignnewValue(self.tree2,None))
        self.tree2 = assignnewValue(self.tree2,self.tree8)
        self.assertEqual(11, self.tree2.value)
        print("Unit test assignNewValue passed")

    def test_isaleaf(self):
       self.assertEqual(False, isaleaf(self.tree1))
       self.assertEqual(True, isaleaf(self.tree2))
       self.assertEqual(False, isaleaf(self.tree3))
       self.assertEqual(False, isaleaf(self.tree4))
       self.assertEqual(False, isaleaf(self.tree5))
       self.assertEqual(False, isaleaf(self.tree6))
       self.assertEqual(False, isaleaf(self.tree7))
       self.assertEqual(False, isaleaf(self.tree8))
       print("Unit test isALeaf passed")

    def test_secondLargestValue(self):
        self.maximum__second_node = secondLargest(self.tree1, self.maximum_node, self.maximum__second_node)
        self.assertEqual(None, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree2, self.maximum_node, self.maximum__second_node)
        self.assertEqual(None, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree3, self.maximum_node, self.maximum__second_node)
        self.assertEqual(100, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree4, self.maximum_node, self.maximum__second_node)
        self.assertEqual(20, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree5, self.maximum_node, self.maximum__second_node)
        self.assertEqual(53, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree6, self.maximum_node, self.maximum__second_node)
        self.assertEqual(55, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree7, self.maximum_node, self.maximum__second_node)
        self.assertEqual(10, secondLargestValue(self.maximum__second_node))
        self.maximum__second_node = secondLargest(self.tree8, self.maximum_node, self.maximum__second_node)
        self.assertEqual(48, secondLargestValue(self.maximum__second_node))
        print("Test secondLargestValue passed")


    def test_maximum_tree(self):
        self.assertEqual(None, maximum_tree(self.tree1,self.maximum_node))
        res_2 = maximum_tree(self.tree2,self.maximum_node)
        self.assertEqual(50,res_2.value)
        res_3 = maximum_tree(self.tree8, self.maximum_node)
        self.assertEqual(55, res_3.value)
        res_4 = maximum_tree(self.tree7, self.maximum_node)
        self.assertEqual(11, res_4.value)
        res_5 = maximum_tree(self.tree6, self.maximum_node)
        self.assertEqual(60, res_5.value)
        print("Test maximum value in a tree passed")

    def test_minimum_tree(self):
        self.assertEqual(None, minimum_tree(self.tree1,self.minimum_node))
        res_2 = minimum_tree(self.tree2,self.minimum_node)
        self.assertEqual(50,res_2.value)
        res_3 = minimum_tree(self.tree8, self.minimum_node)
        self.assertEqual(10, res_3.value)
        res_4 = minimum_tree(self.tree7, self.minimum_node)
        self.assertEqual(7, res_4.value)
        res_5 = minimum_tree(self.tree6, self.minimum_node)
        self.assertEqual(7, res_5.value)
        print("Test minimum value in a tree passed")


    def test_secondSmallestValue(self):
        self.minimum__second_node = secondSmallestValue(self.tree1, self.minimum_node, self.minimum__second_node)
        self.assertEqual(None,  self.minimum__second_node)
        self.minimum__second_node = secondSmallestValue(self.tree2, self.minimum_node, self.minimum__second_node)
        self.assertEqual(None, self.minimum__second_node)
        self.minimum__second_node = secondSmallestValue(self.tree3, self.minimum_node, self.minimum__second_node)
        self.assertEqual(200,self.minimum__second_node.value)
        self.minimum__second_node = secondSmallestValue(self.tree4, self.minimum_node, self.minimum__second_node)
        self.assertEqual(25, self.minimum__second_node.value)
        self.minimum__second_node = secondSmallestValue(self.tree5, self.minimum_node, self.minimum__second_node)
        self.assertEqual(53, self.minimum__second_node.value)
        self.minimum__second_node = secondSmallestValue(self.tree6, self.minimum_node, self.minimum__second_node)
        self.assertEqual(9, self.minimum__second_node.value)
        self.minimum__second_node = secondSmallestValue(self.tree7, self.minimum_node, self.minimum__second_node)
        self.assertEqual(9, self.minimum__second_node.value)
        self.minimum__second_node = secondSmallestValue(self.tree8, self.minimum_node, self.minimum__second_node)
        self.assertEqual(11, self.minimum__second_node.value)

        print("Test second smallest value in a tree passed")






if __name__ == '__main__':
    unittest.main()
