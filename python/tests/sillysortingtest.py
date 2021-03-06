import unittest

from domsort import sillysorting, sortingutil


class SillySortingTest(unittest.TestCase):

    def setUp(self):
        self.items = [9, 1, 6, 3, 5, 8]
        self.sorted_items = [1, 3, 5, 6, 8, 9]
        self.medium_items = [9, 1, 6, -1, 3, 5, 8, 1, 3, 5, 8]
        self.medium_sorted_items = [-1, 1, 1, 3, 3, 5, 5, 6, 8, 8, 9]
        self.long_items = [18, -41, 66, 91, 113, 61, -80, 96, -60, 1, 34, -95, -107, 31, -52, 46, -103, -57, -86, 13, -26, 93, 12, -23, 24, -110, -68, 40, 120, 12, 84, -9, 54, -1, -126, 45, 71, 109, 20, -102, -64, -127, -84, -105, 119, -27, -126, -59, 43, 20, 47, -16, -121, 68, -97, -80, -94, -106, -117, 65, -59, 87, -70, 114, 96, -52, -99, -10, -89, 81, -75, 18, -16, 122, 80, 21, -47, -14, 51, -3, -25, 14, 78, -59, -7, -45, -57, 29, -67, -24, -4, -9, 117, 54, -65, 35, 111, 96, 83, -34, 59, -27, -43, -124, 37, 92, -85, 21, 89, -96, -105, -106, 104, 60, 76, -6, 3, 106, 16, -113, 75, -124, 86, 98, -33, 39, -14, 0, 89, 61, 95, -42, 93, 39, 96, -37, 20, -35, -98, -46, 36, -57, 119, -21, -111, 37, -75, -101, -109, -102, -109, -32, -82, 85, -100, 55, -86, -14, 39, -127, -109, 26, -42, 70, -12, 0, 52, -41, 42, -90, -5, 103, -4, -32, -7, -119, -102, 124, -119, -37, -74, 34, 81, -104, -37, 103, 67, 106, 126, 90, 119, -66, -76, -120, -101, -114, -27, -20, 118, 67, 57, 86, 27, 97, -40, -19, 118, -105, 56, -7, 125, 57, 51, 58, 124, 79, -23, 59, -103, -51, -18, 96, -49, -28, 41, 91, -106, 25, 104, 70, 19, -11, 58, -30, -63, -7, 2, -71, 101, -80, 100, 23, -110, 99, -87, 104, -110, 91, 21, 123, 53, 84, -106, 54, -31, 84, 19, -9, -97, -112, -107, -74, 82, 9, -18, 66, 27, 60, -1, 47, 116, 16, -5, 62, 96, 96, 58, 55, 95, -15, 74, -2, 41, -27, 27, -108, 72, 54, -120, -103, 98, -39, 114, -25, -49, 123, -21, -29, 36, -111, -22, -83, 98, 105, 59, -70, 21, 35, -82, -80, 105, 34, 26, 75, -85, -83, 56, 121, 9, 95, 13, 2, 29, -78, 98, -112, -78, 55, 54, -57, 77, 52, -63, 95, 56, 98, -25, 61, 14, 1, 56, 78, -3, -89, -107, -116, 106, 30, 28, -30, -32, 117, -75, 116, 38, -79, -105, -126, -59, 20, -104, 3, -74, -89, -114, -111, 8, -76, 113, -19, -78, -34, 23, -19, -96, -100, -14, 88, -38, -63, -78, 54, -87, -111, -86, 54, -73, 92, -112, 54, -45, 72, -78, 19, 96, -17, 71, 93, -106, -72, 41, -68, -11, 98, -110, -67, 31, -74, -80, 44, -28, -126, 84, -120, 65, -75, 120, -100, 31, -45, -116, 86, -69, -9, -126, 32, 64, -74, -72, -7, 93, -94, 42, 52, 89, -15, 114, -23, -50, -30, 102, 89, 66, 27, -55, 78, 88, 60, 47, 114, 119, -79, -7, -108, -113, -20, 109, 28, 114, 124, -85, -15, 33, 72, 4, 65, 23, 29, 39, -53, 125, -84, 95, -125, -7, -97, -57, -63, -17, -91, -110, 89, -46, 94, -69, 76, -107, -85, -72, 118, -58, 101, -108, 113, 16, -67, -46, -102, 55, 20]
        self.long_sorted_items = [-127, -127, -126, -126, -126, -126, -126, -125, -124, -124, -121, -120, -120, -120, -119, -119, -117, -116, -116, -114, -114, -113, -113, -112, -112, -112, -111, -111, -111, -111, -110, -110, -110, -110, -110, -109, -109, -109, -108, -108, -108, -107, -107, -107, -107, -106, -106, -106, -106, -106, -105, -105, -105, -105, -104, -104, -103, -103, -103, -102, -102, -102, -102, -101, -101, -100, -100, -100, -99, -98, -97, -97, -97, -96, -96, -95, -94, -94, -91, -90, -89, -89, -89, -87, -87, -86, -86, -86, -85, -85, -85, -85, -84, -84, -83, -83, -82, -82, -80, -80, -80, -80, -80, -79, -79, -78, -78, -78, -78, -78, -76, -76, -75, -75, -75, -75, -74, -74, -74, -74, -74, -73, -72, -72, -72, -71, -70, -70, -69, -69, -68, -68, -67, -67, -67, -66, -65, -64, -63, -63, -63, -63, -60, -59, -59, -59, -59, -58, -57, -57, -57, -57, -57, -55, -53, -52, -52, -51, -50, -49, -49, -47, -46, -46, -46, -45, -45, -45, -43, -42, -42, -41, -41, -40, -39, -38, -37, -37, -37, -35, -34, -34, -33, -32, -32, -32, -31, -30, -30, -30, -29, -28, -28, -27, -27, -27, -27, -26, -25, -25, -25, -24, -23, -23, -23, -22, -21, -21, -20, -20, -19, -19, -19, -18, -18, -17, -17, -16, -16, -15, -15, -15, -14, -14, -14, -14, -12, -11, -11, -10, -9, -9, -9, -9, -7, -7, -7, -7, -7, -7, -7, -6, -5, -5, -4, -4, -3, -3, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 8, 9, 9, 12, 12, 13, 13, 14, 14, 16, 16, 16, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 23, 23, 23, 24, 25, 26, 26, 27, 27, 27, 27, 28, 28, 29, 29, 29, 30, 31, 31, 31, 32, 33, 34, 34, 34, 35, 35, 36, 36, 37, 37, 38, 39, 39, 39, 39, 40, 41, 41, 41, 42, 42, 43, 44, 45, 46, 47, 47, 47, 51, 51, 52, 52, 52, 53, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 57, 57, 58, 58, 58, 59, 59, 59, 60, 60, 60, 61, 61, 61, 62, 64, 65, 65, 65, 66, 66, 66, 67, 67, 68, 70, 70, 71, 71, 72, 72, 72, 74, 75, 75, 76, 76, 77, 78, 78, 78, 79, 80, 81, 81, 82, 83, 84, 84, 84, 84, 85, 86, 86, 86, 87, 88, 88, 89, 89, 89, 89, 89, 90, 91, 91, 91, 92, 92, 93, 93, 93, 93, 94, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 96, 97, 98, 98, 98, 98, 98, 98, 99, 100, 101, 101, 102, 103, 103, 104, 104, 104, 105, 105, 106, 106, 106, 109, 109, 111, 113, 113, 113, 114, 114, 114, 114, 114, 116, 116, 117, 117, 118, 118, 118, 119, 119, 119, 119, 120, 120, 121, 122, 123, 123, 124, 124, 124, 125, 125, 126]

    def test_bubble_sort(self):
        self.assertEqual(self.sorted_items, sillysorting.bubble_sort(self.items))

    def test_bogo_sort(self):
        self.assertEqual(self.sorted_items, sillysorting.bogo_sort(self.items))

    # def test_bogo_sort_medium(self):
    #     self.assertEqual(self.medium_sorted_items, sillysorting.bogo_sort(self.medium_items))

    def test_stalin_sort_long(self):
        self.assertTrue(sortingutil.in_order(sillysorting.stalin_sort(self.long_items)))

if __name__ == '__main__':
    unittest.main()
