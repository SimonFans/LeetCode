class solution(object):

    def minCost(self,costs):

        if len(costs)==0:
            return 0
        cost=[[0 for j in range(3)] for i in range(len(costs))]
        cost[0][0]=costs[0][0]
        cost[0][1] = costs[0][1]
        cost[0][2] = costs[0][2]

        i=1
        while(i<len(costs)):
            cost[i][0] = min(cost[i - 1][1], cost[i - 1][2]) + costs[i][0]
            cost[i][1] = min(cost[i - 1][0], cost[i - 1][2]) + costs[i][1]
            cost[i][2] = min(cost[i - 1][0], cost[i - 1][1]) + costs[i][2]
            i+=1

        return min(cost[i-1][0],cost[i-1][1],cost[i-1][2])



costs=[[1,2,3],[5,6,4],[9,3,5],[8,5,3],[1,5,8]]
test=solution()
print(test.minCost(costs))