class Solution(object):
    def isToeplitzMatrix(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(mat)
        m = len(mat[0])
        ref = []
        for j in range(m-1):
            ref.append(mat[0][j])
        for i in range(1, n):
            ref = [mat[i][0]] + ref
            for j in range(1, m):
                if mat[i][j] != ref[j]:
                    return False
        return True 