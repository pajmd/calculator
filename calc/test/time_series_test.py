import unittest

class TestTimeSerires(unittest.TestCase):
    def setUp(self):
        self.SERIES1 = ['1', '2', '3']
        self.SERIES2 = ['11', '12', '13']
        self.res = ['12.0', '14.0', '16.0']

    def test_adding_2_series(self):
        for v1, v2 in zip(self.SERIES1, self.SERIES2):
            print('{} {}'.format(v1, v2))
        l = [str(float(v1) + float(v2)) for v1, v2 in zip(self.SERIES1, self.SERIES2)]
        self.assertEqual(self.res, l)
