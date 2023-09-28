# solved by Ahmed Hamdy
class MoveZero:
    def __init__(self, nums):
        self.nums = nums

    def moveZero(self, nums):
        right = []
        left = []
        zero = []
        for i in range(len(self.nums)):
                if self.nums[i] == 0:
                        right.insert(-i, self.nums[i])
                else:
                        left.insert(i, self.nums[i])
        zero= left + right
#       move.reverse()

        return zero


#     0  1  2   3
#     -4 -3 -2 -1
nm = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

print(MoveZero(nm).moveZero(nm))
