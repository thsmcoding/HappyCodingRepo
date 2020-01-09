import unittest
from solution.gasstation_module import find_nextstation
from solution.gasstation_module import checking_circuit
from solution.gasstation_module import minimumgasstation_index


class MyTestGasStation(unittest.TestCase):
    def setUp(self):
        self.totalStations = 10
        self.station1 = 12
        self.station2 = 10
        self.station3 = 0
        self.station4 = 9
        self.station5 = 5
        self.A = [1,2]
        self.B = [2,1]
        print("Test initialization done")


    def test_findnextstation(self):
        self.assertEqual(-1, find_nextstation(self.station1, self.totalStations))
        self.assertEqual(-1, find_nextstation(self.station2, self.totalStations))
        self.assertEqual(1, find_nextstation(self.station3, self.totalStations))
        self.assertEqual(0, find_nextstation(self.station4, self.totalStations))
        self.assertEqual(6, find_nextstation(self.station5, self.totalStations))
        print("Unit test next station passed")


    def test_checking_circuit(self):
        result_station1 = checking_circuit(0, self.A, self.B)
        result_station2 = checking_circuit(1, self.A, self.B)
        self.assertEqual(False, result_station1)
        self.assertEqual(True, result_station2)
        print("Unit test checking circuit passed")

    def test_minimumgasstation_index(self):
        min_gasstation = minimumgasstation_index(self.A, self.B)
        self.assertEqual(1, min_gasstation)
        print("Unit test minimumgaststation passed")







if __name__ == '__main__':
    unittest.main()
