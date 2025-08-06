
class R_cube:

    def __init__(self, up_face=None, left_face=None, front_face=None, right_face=None, back_face=None, down_face=None):

        # Defualt Values
        if up_face is None:
            up_face = [["W", "W", "W"] for i in range(3)]
        if left_face is None:
            left_face = [["O", "O", "O"] for i in range(3)]
        if front_face is None:
            front_face = [["G", "G", "G"] for i in range(3)]
        if right_face is None:
            right_face = [["R", "R", "R"] for i in range(3)]
        if back_face is None:
            back_face = [["B", "B", "B"] for i in range(3)]
        if down_face is None:
            down_face = [["Y", "Y", "Y"] for i in range(3)]

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
        for i in range(18):
            print(" ", end='')


        print(self.up_face[0][:3])


        for i in range(18):
            print(" ", end='')


        print(self.up_face[1][:3])


        for i in range(18):
            print(" ", end='')


        print(self.up_face[2][:3])


        print()


        # Print Middle Grids
    # _______________________________________________

        print(self.left_face[0][:3], end='')
        print("   ", end='')
        print(self.front_face[0][:3], end='')
        print("   ", end='')
        print(self.right_face[0][:3], end='')
        print("   ", end='')
        print(self.back_face[0][:3])


        print(self.left_face[1][:3], end='')
        print("   ", end='')
        print(self.front_face[1][:3], end='')
        print("   ", end='')
        print(self.right_face[1][:3], end='')
        print("   ", end='')
        print(self.back_face[1][:3])


        print(self.left_face[2][:3], end='')
        print("   ", end='')
        print(self.front_face[2][:3], end='')
        print("   ", end='')
        print(self.right_face[2][:3], end='')
        print("   ", end='')
        print(self.back_face[1][:3])

        print()

        # Print Bottom Grid
    # _______________________________________________

        for i in range(18):
            print(" ", end='')

        print(self.down_face[0][:3])

        for i in range(18):
            print(" ", end='')


        print(self.down_face[1][:3])

        for i in range(18):
            print(" ", end='')


        print(self.down_face[2][:3])