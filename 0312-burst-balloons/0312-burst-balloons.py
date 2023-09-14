class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1] # Add 1 to the beginning and end of the array
        dp = [[0] * (n+2) for _ in range(n+2)] # Initialize dp array
        
        for length in range(1, n+1): # Iterate over all possible subarray lengths
            for i in range(1, n-length+2): # Iterate over all possible subarray starting positions
                j = i + length - 1 # Calculate the ending position of the subarray
                for k in range(i, j+1): # Iterate over all possible balloon burst positions
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]) # Update dp array
        
        return dp[1][n] # Return the maximum coins for the entire array