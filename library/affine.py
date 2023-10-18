

def mat_mul(A, B):
    y, x = len(A), len(A[0])
    yy, xx = len(B), len(B[0])
    if not yy == x:
        raise Exception(
            '({}, {}) and ({}, {}) cannot be multipled'.format(y, x, yy, xx))
    mat = [[0] * xx for _ in range(y)]
    for i in range(y):
        for j in range(xx):
            mat[i][j] = sum(A[i][k] * B[k][j] for k in range(x))
    return mat


class Affine:
    def __init__(self, N):
        self.mat = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

    @staticmethod
    def get(A, x, y):
        M = [
            [x],
            [y],
            [1]
        ]
        M = mat_mul(A, M)
        return (M[0][0], M[1][0])

    # clock wise
    def rot90(self):
        self.mat = mat_mul(
            [
                [0, 1, 0],
                [-1, 0, 0],
                [0, 0, 1]
            ],
            self.mat
        )

    # counter clock wise
    def rot90_counter(self):
        self.mat = mat_mul(
            [
                [0, -1, 0],
                [1, 0, 0],
                [0, 0, 1]
            ],
            self.mat
        )

    def add_x(self, t):
        self.mat = mat_mul(
            [
                [1, 0, t],
                [0, 1, 0],
                [0, 0, 1]
            ],
            self.mat
        )

    def add_y(self, t):
        self.mat = mat_mul(
            [
                [1, 0, 0],
                [0, 1, t],
                [0, 0, 1]
            ],
            self.mat
        )

    def minus_x(self):  # x -> -x
        self.mat = mat_mul(
            [
                [-1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ],
            self.mat
        )

    def minus_y(self):  # y -> -y
        self.mat = mat_mul(
            [
                [1, 0, 0],
                [0, -1, 0],
                [0, 0, 1]
            ],
            self.mat
        )


N = 3
affine = Affine(N)
