class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = ""
        s = s.upper()
        l = s.split('-')
        new_s = ''.join(l)
        
        remaining = len(new_s) % k
        n = len(new_s) // k
        
        if remaining > 0 and n > 0:
            result += new_s[:remaining] + '-'
            new_s = new_s[remaining:]
        elif n == 0:
            result += new_s
            new_s = ""

        for i in range(n-1):
            result += new_s[k * i : k * (i+1)] + '-'
        result += new_s[k * (n-1) : ]
        
        return result