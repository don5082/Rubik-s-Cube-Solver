import unittest
import Cube
from Cube import Color

testing_cube = Cube.R_cube(
                            [[Color.R, Color.R, Color.W],
                                     [Color.W, Color.W, Color.Y],
                                     [Color.O, Color.W, Color.O]],

                           [[Color.Y, Color.O, Color.Y],
                                    [Color.O, Color.O, Color.B],
                                    [Color.B, Color.O, Color.R]],

                           [[Color.G, Color.G, Color.G],
                                     [Color.Y, Color.G, Color.Y],
                                     [Color.G, Color.W, Color.Y]],

                           [[Color.W, Color.R, Color.B],
                                     [Color.G, Color.R, Color.R],
                                     [Color.R, Color.R, Color.B]],

                           [[Color.W, Color.B, Color.B],
                                      [Color.G, Color.Y, Color.B],
                                      [Color.R, Color.Y, Color.Y]],

                           [[Color.W, Color.O, Color.O],
                                     [Color.B, Color.B, Color.W],
                                     [Color.G, Color.G, Color.O]])



class TestMoves(unittest.TestCase):


    def test_R(self):
        test_c = testing_cube.deep_cpy_cube()
        test_c.R()
        correct_cube = Cube.R_cube(
                            [[Color.R, Color.R, Color.G],
                                     [Color.W, Color.W, Color.Y],
                                     [Color.O, Color.W, Color.Y]],

                           [[Color.Y, Color.O, Color.Y],
                                    [Color.O, Color.O, Color.B],
                                    [Color.B, Color.O, Color.R]],

                           [[Color.G, Color.G, Color.B],
                                     [Color.Y, Color.G, Color.B],
                                     [Color.G, Color.W, Color.Y]],

                           [[Color.R, Color.G, Color.W],
                                     [Color.R, Color.R, Color.R],
                                     [Color.B, Color.R, Color.B]],

                           [[Color.W, Color.B, Color.O],
                                      [Color.G, Color.Y, Color.W],
                                      [Color.R, Color.Y, Color.O]],

                           [[Color.W, Color.O, Color.W],
                                     [Color.B, Color.B, Color.Y],
                                     [Color.G, Color.G, Color.O]])


        self.assertEqual(correct_cube.up_face, test_c.up_face)  # add assertion here
        self.assertEqual(correct_cube.left_face, test_c.left_face)  # add assertion here
        self.assertEqual(correct_cube.front_face, test_c.front_face)  # add assertion here
        self.assertEqual(correct_cube.right_face, test_c.right_face)  # add assertion here
        self.assertEqual(correct_cube.down_face, test_c.down_face)  # add assertion here
        self.assertEqual(correct_cube.back_face, test_c.back_face)  # add assertion here


    def test_Rprime(self):
        test_c = testing_cube.deep_cpy_cube()
        test_c.Rprime()

        correct_cube = Cube.R_cube(
            [[Color.R, Color.R, Color.O],
                     [Color.W, Color.W, Color.W],
                     [Color.O, Color.W, Color.O]],

            [[Color.Y, Color.O, Color.Y],
                     [Color.O, Color.O, Color.B],
                     [Color.B, Color.O, Color.R]],

            [[Color.G, Color.G, Color.W],
                      [Color.Y, Color.G, Color.Y],
                      [Color.G, Color.W, Color.O]],

            [[Color.B, Color.R, Color.B],
                      [Color.R, Color.R, Color.R],
                      [Color.W, Color.G, Color.R]],

            [[Color.W, Color.B, Color.G],
                       [Color.G, Color.Y, Color.Y],
                       [Color.R, Color.Y, Color.Y]],

            [[Color.W, Color.O, Color.B],
                      [Color.B, Color.B, Color.B],
                      [Color.G, Color.G, Color.Y]])


        self.assertEqual(correct_cube.up_face, test_c.up_face)
        self.assertEqual(correct_cube.left_face, test_c.left_face)
        self.assertEqual(correct_cube.front_face, test_c.front_face)
        self.assertEqual(correct_cube.right_face, test_c.right_face)
        self.assertEqual(correct_cube.down_face, test_c.down_face)
        self.assertEqual(correct_cube.back_face, test_c.back_face)

    def test_L(self):
        test_c = testing_cube.deep_cpy_cube()
        test_c.L()
        correct_cube = Cube.R_cube(
            [[Color.W, Color.R, Color.W],
                    [Color.B, Color.W, Color.Y],
                    [Color.G, Color.W, Color.O]],

            [[Color.B, Color.O, Color.Y],
                     [Color.O, Color.O, Color.O],
                     [Color.R, Color.B, Color.Y]],

            [[Color.R, Color.G, Color.G],
                      [Color.W, Color.G, Color.Y],
                      [Color.O, Color.W, Color.Y]],

            [[Color.W, Color.R, Color.B],
                      [Color.G, Color.R, Color.R],
                      [Color.R, Color.R, Color.B]],

            [[Color.G, Color.B, Color.B],
                      [Color.Y, Color.Y, Color.B],
                      [Color.G, Color.Y, Color.Y]],

            [[Color.W, Color.O, Color.O],
                      [Color.G, Color.B, Color.W],
                      [Color.R, Color.G, Color.O]])

        self.assertEqual(correct_cube.up_face, test_c.up_face)
        self.assertEqual(correct_cube.left_face, test_c.left_face)
        self.assertEqual(correct_cube.front_face, test_c.front_face)
        self.assertEqual(correct_cube.right_face, test_c.right_face)
        self.assertEqual(correct_cube.down_face, test_c.down_face)
        self.assertEqual(correct_cube.back_face, test_c.back_face)

    def test_Lprime(self):
        self.assertEqual(True, False)  # add assertion here




if __name__ == '__main__':
    unittest.main()
