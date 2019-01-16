Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        for p in points:
            cmap={}
            for q in points:
                dis=(p[0]-q[0])**2+(p[1]-q[1])**2
                cmap[dis]=cmap.get(dis,0)+1
            # cmap[i]-1是为了去除掉只有一个成立的点
            for i in cmap:
                res+=(cmap[i])*(cmap[i]-1)
        return res
