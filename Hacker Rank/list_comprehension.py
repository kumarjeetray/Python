'''
Let's learn about list comprehensions! You are given three x,y and z integers and representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of is not equal to n.
Please use list comprehensions rather than multiple loops, as a learning exercise.
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    sides = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    sides.append([i, j, k])
    print(sides)
