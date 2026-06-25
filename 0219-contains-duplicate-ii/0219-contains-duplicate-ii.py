class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in visited:
                visited[num] = i
            else:
                if i - visited[num] <= k:
                    return True
                visited[num] = i
        return False