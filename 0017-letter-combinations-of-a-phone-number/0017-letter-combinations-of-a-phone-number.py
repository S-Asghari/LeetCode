class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # ----------
        # Solution 1
        # ----------
        # mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        # res = [""]
        # for d in digits:
        #     temp_res = []
        #     for letter in res:
        #         for c in mapping[int(d)]:
        #             temp_res.append(letter + c)
        #     res = temp_res
        # return res
        # ----------
        # Solution 2
        # ----------
        res = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(d, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in mapping[digits[d]]:
                backtrack(d + 1, curStr + c)
        
        backtrack(0, "")
        return res