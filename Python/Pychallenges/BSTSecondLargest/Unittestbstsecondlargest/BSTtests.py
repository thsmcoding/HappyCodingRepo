import unittest
from Solution.BSTPackage.BinaryTreeNode import BinaryTreeNode
from Solution.BSTPackage.BSTModulefunctions import isaleaf
from Solution.BSTPackage.BSTModulefunctions import secondLargest
from Solution.BSTPackage.BSTModulefunctions import secondLargestValue
from Solution.BSTPackage.BSTModulefunctions import assignnewValue

class MyTestBstclass(unittest.TestCase):
    def setUp(self):
        self.maximum_node = None
        self.maximum__second_node = None

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


    def test_assignNewValue(self):
        self.assertEqual(None, assignnewValue(self.tree1,self.tree2))
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


if __name__ == '__main__':
    unittest.main()
