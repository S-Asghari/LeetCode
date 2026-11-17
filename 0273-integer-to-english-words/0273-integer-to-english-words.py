class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: 
            return "Zero"
        
        ones = { 
            1: "One", 
            2: "Two", 
            3: "Three", 
            4: "Four", 
            5: "Five", 
            6: "Six", 
            7: "Seven", 
            8: "Eight", 
            9: "Nine",
            10: "Ten", 
            11: "Eleven", 
            12: "Twelve", 
            13: "Thirteen", 
            14: "Fourteen", 
            15: "Fifteen", 
            16: "Sixteen", 
            17: "Seventeen", 
            18: "Eighteen", 
            19: "Nineteen"
        }

        tens = {
            20: "Twenty", 
            30: "Thirty", 
            40: "Forty", 
            50: "Fifty", 
            60: "Sixty", 
            70: "Seventy", 
            80: "Eighty", 
            90: "Ninety",
        }

        def convertSubNum(n) -> str: # n = left middle right
            res = []
            
            left = n // 100
            if left:
                res.append(ones[left] + " Hundred")
            
            middle_right = n % 100
            if middle_right >= 20:
                middle, right = (middle_right // 10) * 10, middle_right % 10
                res.append(tens[middle])
                if right:
                    res.append(ones[right])
            elif middle_right:
                res.append(ones[middle_right])
            
            return " ".join(res)
            
        
        level = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []

        while num:
            sub_num = num % 1000
            s = convertSubNum(sub_num)
            if s:
                res.append(s + level[i])
            num = num // 1000
            i += 1

        res.reverse()
        return " ".join(res)