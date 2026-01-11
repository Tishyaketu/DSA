class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        k=len(m)
        l=0
        r=k-1
        while(l<r):
            m[l],m[r]=m[r],m[l]
            l+=1
            r-=1
        for i in range(k):
            for j in range(i):#why is j in range(i) and not range(k)?
                if(i!=j):
                    m[i][j],m[j][i]=m[j][i],m[i][j]