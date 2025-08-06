class Rubiks_cube:
    def __init__(self, up_face, left_face, front_face, right_face, back_face, down_face):
        self.up_face = up_face
        self.left_face = left_face
        self.front_face = front_face
        self.right_face = right_face
        self.back_face = back_face
        self.down_face = down_face

    def print_cube(self, Rubiks_cube):

        # Print Top grid
    # ___________________________
        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.up_face[0][:2])


        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.up_face[1][:2])


        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.up_face[2][:2])


        # Print Middle Grids
    # _______________________________________________

        print(Rubiks_cube.left_face[0][:2], end='')
        print(Rubiks_cube.front_face[0][:2], end='')
        print(Rubiks_cube.right_face[0][:2], end='')
        print(Rubiks_cube.back_face[0][:2])

        print(Rubiks_cube.left_face[1][:2], end='')
        print(Rubiks_cube.front_face[1][:2], end='')
        print(Rubiks_cube.right_face[1][:2], end='')
        print(Rubiks_cube.back_face[1][:2])

        print(Rubiks_cube.left_face[2][:2], end='')
        print(Rubiks_cube.front_face[2][:2], end='')
        print(Rubiks_cube.right_face[2][:2], end='')
        print(Rubiks_cube.back_face[1][:2])

        # Print Bottom Grid
    # _______________________________________________

        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.down_face[0][:2])

        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.down_face[1][:2])

        print(' ', end='')
        print(' ', end='')
        print(' ', end='')

        print(Rubiks_cube.down_face[2][:2])