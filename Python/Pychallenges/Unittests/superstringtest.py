import io
import unittest
import unittest.mock
from ChallengeModule.superstring import checking
from ChallengeModule.superstring import reducingliste
from ChallengeModule.superstring import superreducingstring
from ChallengeModule.superstring import cutting


class MyTestSuperString(unittest.TestCase):
    def test_checking(self):
        case1 = ""
        case1_ans = checking(case1)
        self.assertEqual(False, case1_ans, "Should be False")

        case2="abcdeojnfb"
        case2_ans = checking(case2)
        self.assertEqual(False, case2_ans, "Should be False")

        case3 = "ccedhy"
        case3_ans = checking(case3)
        self.assertEqual(True, case3_ans,"Should be True")

        case4 = "y"
        case4_ans = checking(case4)
        self.assertEqual(False, case4_ans, "Should be False")

        print("Function checking ---> OK")

    def test_reducingstring(self):
        case1 = []
        case1_ans = reducingliste(case1)
        self.assertEqual(True, case1_ans, "Should be True")

        case2 = ['a','b','e']
        case2_ans = reducingliste(case2)
        self.assertEqual(False, case2_ans, "Should be True")

        case3 = ['a','a','z','f','e']
        case3_ans = reducingliste(case3)
        self.assertEqual(True, case3_ans, "Should be True")

        case4 = ['a','b','z','z','f','e']
        case4_ans = reducingliste(case4)
        self.assertEqual(True, case4_ans, "Should be True")

        case5 = ['a', 'b', 'z', 'd', 'f', 'f']
        case5_ans = reducingliste(case5)
        self.assertEqual(True, case5_ans, "Should be True")

        case6 = ['h']
        case6_ans = reducingliste(case6)
        self.assertEqual(False, case6_ans, "Should be False")

        print("Function reducingliste ---> OK")

    def test_cutting(self):
        caseliste = []
        case1_s = "abc"
        cutting(caseliste, case1_s)
        case1_ans = len(caseliste)
        self.assertEqual(3, case1_ans, "List should have 3 elements")

        case2_s = ""
        caseliste = []
        cutting(caseliste, case2_s)
        case2_ans = len(caseliste)
        self.assertEqual(0, case2_ans, "List should be empty")

        case3_s = "aaabccddd"
        caseliste = []
        cutting(caseliste, case3_s)
        case3_ans = len(caseliste)
        self.assertEqual(3, case3_ans, "List should have 3 elements")

        case4_s = "aa"
        caseliste = []
        cutting(caseliste, case4_s)
        case4_ans = len(caseliste)
        self.assertEqual(0, case4_ans, "List should have no elements")

        case5_s = "baab"
        caseliste = []
        cutting(caseliste, case5_s)
        case5_ans = len(caseliste)
        self.assertEqual(2, case5_ans, "List should have 2 elements")
        print("Function cutting ---> OK")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, str, expectedOutput, mock_stdout):
        superreducingstring(str)
        self.assertEqual(mock_stdout.getvalue(),expectedOutput)


    def test_superreducingstring(self):
        str_1 = "aaabccddd"
        expected_1 = "abd"
        self.assert_stdout(str_1,expected_1)

        str_2 = "baab"
        expected_2 = "Empty String"
        self.assert_stdout(str_2, expected_2)

        str_3 = "aa"
        expected_3 = "Empty String"
        self.assert_stdout(str_3, expected_3)

        print("Function superreducingstring ---> OK")


if __name__ == '__main__':
    unittest.main()
