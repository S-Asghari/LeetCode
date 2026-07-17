class Solution:
    def decodeString(self, s: str) -> str:
        # decoded_str = ""
        l = list(s)
        # while l:
        #     c = l.pop()
        #     if c == ']':
        #         encoded_str = ""
        #         while l[-1] != '[':
        #             encoded_str = l.pop() + encoded_str
        #         l.pop() # '['
        #         k = ""
        #         while l and '0' <= l[-1] <= '9':
        #             k = l.pop() + k
        #         k = int(k)
        #         decoded_str = encoded_str * k + decoded_str
        #     elif 'a' <= c <= 'z':
        #             decoded_str = c + decoded_str
        
        def recursive(l):
            decoded_l = []
            
            while l:
                k = ""
                while '0' <= l[0] <= '9':
                    k += l.pop(0)
                k = int(k) if k != "" else 1
                # print(k)

                brackets = 0
                if l[0] == '[' :
                    brackets += 1
                    l.pop(0)
                    inner_l = []
                    while not (brackets == 1 and l[0] == ']'):
                        if l[0] == '[':
                            brackets += 1
                        elif l[0] == ']':
                            brackets -= 1
                        inner_l.append(l.pop(0))
                    l.pop(0)
                    decoded_inner_l = recursive(inner_l)
                    # print(f'inner_l = {inner_l}')
                    # print(f'decoded_inner_l = {decoded_inner_l}')
                    # print(f'l = {l}')
                    decoded_l += k * decoded_inner_l
                    # print(f'decoded_l = {decoded_l}')
                
                elif 'a' <= l[0] <= 'z':
                    decoded_l.append(l.pop(0))

            return decoded_l
            
        return ''.join(recursive(l))
        
        # return decoded_str