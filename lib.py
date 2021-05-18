from math import floor


class LowLevelCubicInterpolate:
    def __init__(self, arr):
        assert len(arr) == 4

        f0 = arr[1]
        f1 = arr[2]
        f0_ = (arr[2] - arr[0])/2
        f1_ = (arr[3] - arr[1])/2

        self.a = 2*f0 - 2*f1 + f0_ + f1_
        self.b = -3*f0 + 3*f1 - 2*f0_ - f1_
        self.c = f0_
        self.d = f0

        # self.a = -(1 / 2) * arr[0] + (3 / 2) * arr[1] - (3 / 2) * arr[2] + (1 / 2) * arr[3]
        # self.b = arr[0] - (5 / 2) * arr[1] + 2 * arr[2] - (1 / 2) * arr[3]
        # self.c = (-1 / 2) * arr[0] + (1 / 2) * arr[2]
        # self.d = arr[1]

    def use(self, x):
        return self.a * (x ** 3) + \
               self.b * (x ** 2) + \
               self.c * x + \
               self.d


class CubicInterpolate:
    def __init__(self, array):
        self.array = array

    def use(self, x):
        assert 0 <= x < len(self.array) - 1
        if x.is_integer():
            return self.array[int(x)]
        point = floor(x)
        work_array = self.array[point - 1:point + 3]
        interpolator = LowLevelCubicInterpolate(work_array)
        return interpolator.use(x % 1)
