class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = [""]
        for d in digits:
            temp_res = []
            for letter in res:
                for c in mapping[int(d)]:
                    temp_res.append(letter + c)
            res = temp_res
        return res
