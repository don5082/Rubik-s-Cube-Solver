import copy
from enum import Enum


class R_cube:

    def __init__(self, up_face=None, left_face=None, front_face=None, right_face=None, back_face=None, down_face=None):

        # Defualt Values
        if up_face is None:
            up_face = [[Color.W, Color.W, Color.W] for i in range(3)]
        if left_face is None:
            left_face = [[Color.O, Color.O, Color.O] for i in range(3)]
        if front_face is None:
            front_face = [[Color.G, Color.G, Color.G] for i in range(3)]
        if right_face is None:
            right_face = [[Color.R, Color.R, Color.R] for i in range(3)]
        if back_face is None:
            back_face = [[Color.B, Color.B, Color.B] for i in range(3)]
        if down_face is None:
            down_face = [[Color.Y, Color.Y, Color.Y] for i in range(3)]

        #Custom Values
        self.up_face = up_face
        self.left_face = left_face
        self.front_face = front_face
        self.right_face = right_face
        self.back_face = back_face
        self.down_face = down_face

    def print_cube(self):

        # Print Top grid
    # ___________________________
        for j in range(3):
            for i in range(9):
                print(" ", end='')

            for i in range(3):
                print(self.up_face[j][i].name, end=' ')
            print()

        # Print Middle Grids
    # _______________________________________________

        for j in range(3):
            print("   ")
            for i in range(3):
                print(self.left_face[j][i].name, end=' ')

            print("   ", end='')
            for i in range(3):
                print(self.front_face[j][i].name, end=' ')

            print("   ", end='')
            for i in range(3):
                print(self.right_face[j][i].name, end=' ')

            print("   ", end='')
            for i in range(3):
                print(self.back_face[j][i].name, end=' ')

        print()
        print()

        # Print Bottom Grid
    # _______________________________________________

        for j in range(3):
            for i in range(9):
                print(" ", end='')

            for i in range(3):
                print(self.down_face[j][i].name, end=' ')
            print()



    def deep_cpy_cube(self):
        og_up = copy.deepcopy(self.up_face)
        og_left = copy.deepcopy(self.left_face)
        og_front = copy.deepcopy(self.front_face)
        og_right = copy.deepcopy(self.right_face)
        og_back = copy.deepcopy(self.back_face)
        og_down = copy.deepcopy(self.down_face)

        return R_cube(og_up, og_left, og_front, og_right, og_back, og_down)


    def Uprime(self):
        original = self.deep_cpy_cube()
        for i in range(3):
            self.front_face[0][i] = original.left_face[0][i]
            self.right_face[0][i] = original.front_face[0][i]
            self.back_face[0][i] = original.right_face[0][i]
            self.left_face[0][i] = original.back_face[0][i]

    def U(self):
        original = self.deep_cpy_cube()
        for i in range(3):
            self.left_face[0][i] = original.front_face[0][i]
            self.back_face[0][i] = original.left_face[0][i]
            self.right_face[0][i] = original.back_face[0][i]
            self.front_face[0][i] = original.right_face[0][i]

class Color(Enum):
    W = 1
    O = 2
    G = 3
    R = 4
    B = 5
    Y = 6