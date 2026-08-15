class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        imin, imax = 0, len(matrix)-1
        jmin, jmax = 0, len(matrix[0])-1
        res = []

        i , j = imin, jmin
        while imin <= i <= imax and jmin <= j <= jmax:
            # left to right
            while j <= jmax:
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            imin = min(imin+1, imax)
            if i > imax: break
            
            # top to buttom
            while i <= imax:
                res.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            jmax = max(jmax-1, jmin)
            if j < jmin: break

            # right to left
            while j >= jmin:
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            imax = max(imax-1, imin)
            if i < imin: break

            # buttom to top
            while i >= imin:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            jmin = min(jmin+1, jmax)
            if i > imax: break

        return res