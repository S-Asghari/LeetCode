class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s: # email address
            s = s.lower()
            name = s.split('@')[0]
            domain = s.split('@')[1]
            s = name[0] + "*****" + name[-1] + "@" + domain
        
        else: # phone number
            new_s = ""
            for char in s:
                if '0' <= char <= '9':
                    new_s += char
            s = new_s[:]
            s = "***-***-" + s[-4:]
            if len(new_s) > 10:
                s = "+" + "*" * (len(new_s) - 10) + "-" + s 

        return s