class ListSum:

    def __init__(self,nums):
        self.nums=nums

    def sum(self,start_idx,end_idx):
        sum = 0
        for i in range(start_idx,end_idx):
            sum =  sum + self.nums[i]
        return sum
print(ListSum([1,2,3,4,5,6,7]).sum(2,5))
