## Prolem 0 Asked by `Apple` (Optimize the sum )
 - Solved by `Ahmed Hamdy`
 
 ```
# List Sum Optimization

This project contains code for optimizing the sum of a list of numbers. The code is written in Python and uses the Wing IDE.

## Step 1: Create a ListSum class

The first step is to create a ListSum class. This class will contain the method that we will use to optimize the sum of a list of numbers.

```python
class ListSum:
    
    def __init__(self,nums):
        self.nums=nums
        
    def sum(self,start_idx,end_idx):
        sum = 0
        for i in range(start_idx,end_idx):
            sum =  sum + self.nums[i]
        return sum
```

## Step 2: Optimize the sum method

The next step is to optimize the sum method. We can do this by using a technique called memoization. Memoization is a technique that stores the results of a function call so that they can be reused later. This can save time if the function is called multiple times with the same arguments.

To use memoization, we will add a dictionary to the ListSum class. This dictionary will store the results of the sum method for each pair of start and end indices.

```python
class ListSum:
    
    def __init__(self,nums):
        self.nums=nums
        self.memo = {}
        
    def sum(self,start_idx,end_idx):
        if (start_idx, end_idx) in self.memo:
            return self.memo[(start_idx, end_idx)]
        else:
            sum = 0
            for i in range(start_idx,end_idx):
                sum =  sum + self.nums[i]
            self.memo[(start_idx, end_idx)] = sum
            return sum
```

## Step 3: Test the optimized sum method

The final step is to test the optimized sum method. We can do this by creating a ListSum object and then calling the sum method with different pairs of start and end indices.

```python
list_sum = ListSum([1,2,3,4,5,6,7])

print(list_sum.sum(2,5))
# Output: 12
```

