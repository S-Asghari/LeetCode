class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # O(n^2) Solution:
        # n = len(nums)
        # reverse_pairs = 0
        # for j in range(n-1, 0, -1):
        #     for i in range(j-1, -1, -1):
        #         if nums[i] > 2* nums[j]:
        #             reverse_pairs += 1
        # return reverse_pairs

        def merge(l, r):
            m = (l+r) // 2

            cnt = 0
            j = m+1
            for i in range(l, m+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (m+1)
            
            i, j = l, m+1
            # print(f"merging {nums[l:m+1]} with {nums[m+1:r+1]}")
            new_arr = []
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    new_arr.append(nums[i])
                    i += 1
                else:
                    new_arr.append(nums[j])
                    j += 1
            new_arr += nums[i:m+1]
            new_arr += nums[j:r+1]
            nums[l:r+1] = new_arr

            return cnt


        def sort(l, r):
            if l >= r:
                return 0
            
            m = (l+r) // 2
            cnt1 = sort(l, m)
            cnt2 = sort(m+1, r)
            cnt3 = merge(l, r)

            return cnt1 + cnt2 + cnt3

        n = len(nums)
        return sort(0, n-1)