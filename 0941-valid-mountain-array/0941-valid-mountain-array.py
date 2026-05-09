class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        reachedPick = False
        prevValue = arr.pop()
        
        while arr and not reachedPick:
            currentValue = arr.pop()
            if currentValue > prevValue:
                prevValue = currentValue
            elif currentValue == prevValue:
                return False
            else:
                reachedPick = True
                arr.append(currentValue)
        
        if not reachedPick or len(arr) == n-1:
            return False
        
        while arr:
            currentValue = arr.pop()
            if currentValue < prevValue:
                prevValue = currentValue
            else:
                return False

        return True
