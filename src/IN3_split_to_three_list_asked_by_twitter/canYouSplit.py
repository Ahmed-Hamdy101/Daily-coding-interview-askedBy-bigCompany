class Solution(object):
    def canPick2(self, arr):
        total_sum = sum(arr)
        print(total_sum)
        # Check if the total sum is divisible by 3
        # if total_sum % 3 != 0:
        #     return False

        target_sum = total_sum // 3
        print(target_sum)
        current_sum = 0
        count = 0

        for i in range(len(arr)):
            current_sum += arr[i]
            print('current_sum=',current_sum)
            # If the current sum equals the target sum, reset for the next partition
            if current_sum == target_sum:
                current_sum = 0
                count += 1

            # If two partitions are found, return True
            if count == 2:
                return True

        # If we reach this point, two partitions were not found
        print('c=',count)
        print('target_sum=',target_sum)
        return False

# Example usage:
solution = Solution()
print(solution.canPick2([2, 4, 3, 3, 2, 2, 2]))  # True
# print(solution.canPick2([1, 2, 3, 4, 5]))  # False
