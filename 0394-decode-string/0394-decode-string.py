class Solution:
    def decodeString(self, s: str) -> str:
        l = list(s)
        
        def recursive(l):
            decoded_l = []
            
            while l:
                # 1.
                k = ""
                while '0' <= l[0] <= '9':
                    k += l.pop(0)
                k = int(k) if k != "" else 1

                # 2.
                brackets = 0
                if l[0] == '[' :
                    brackets += 1
                    l.pop(0)
                    inner_l = []
                    while not (brackets == 1 and l[0] == ']'):
                        if l[0] == '[': brackets += 1
                        elif l[0] == ']': brackets -= 1
                        inner_l.append(l.pop(0))
                    l.pop(0)
                    decoded_inner_l = recursive(inner_l)
                    decoded_l += k * decoded_inner_l
                
                # 3.
                while l and 'a' <= l[0] <= 'z':
                    decoded_l.append(l.pop(0))

            return decoded_l
            
        return ''.join(recursive(l))