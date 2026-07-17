class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        def backtrack(r, comb):
            if len(comb) == 4 and r == "":
                results.append('.'.join(comb))
                return
            elif len(comb) == 4 or r == "":
                return
            
            num_choices = max(0, len(r) - (4-len(comb)) + 1)
            for i in range(0, min(3, num_choices)):
                if r[0] == '0' and i > 0:
                    continue
                if int(r[0:i+1]) > 255:
                    continue
                comb.append(r[0:i+1])
                backtrack(r[i+1:], comb)
                comb.pop()
                
        backtrack(s, [])
        return results