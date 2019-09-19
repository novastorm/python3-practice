'''
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.

Here's a starting point:

def max_subarray_sum(arr):
  # Fill this in.

print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137
'''

class Solution:
    def maxSubArraySum(arr):
        maxSofar = arr[0]
        currMax = arr[0]

        print(currMax, maxSofar)
        for n in arr[1:]:
            currMax = max(n, currMax + n)
            maxSofar = max(maxSofar, currMax)
            print(currMax, maxSofar)

        return maxSofar


if __name__ == '__main__':
    results = Solution.maxSubArraySum([34, -50, 42, 14, -5, 86])
    print(results == 137)
    results = Solution.maxSubArraySum([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    print(results == -3)
    results = Solution.maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3] )
    print(results == 7)