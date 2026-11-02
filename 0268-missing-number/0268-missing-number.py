class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expectedTotal = n * (n+1) // 2
        actualTotal = sum(nums)
        return expectedTotal - actualTotal
    
# def run_tests() -> None:
#     solution = Solution()
#     assert solution.missingNumber([3, 0, 1]) == 2, "Test 1 failed"
#     assert solution.missingNumber([0, 1]) == 2, "Test 2 failed"
#     assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8, "Test 3 failed"
#     assert solution.missingNumber([1]) == 0, "Test 4 failed"
#     assert solution.missingNumber([0]) == 1, "Test 5 failed"
#     print("All tests passed successfully!")

# if __name__ == "__main__":
#     run_tests()