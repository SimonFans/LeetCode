There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]



import heapq
import collections
inputs = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
result=dict()
heap=collections.defaultdict(list)
for i in range(len(inputs)):
    if inputs[i][0] not in heap:
        heap[inputs[i][0]]=[inputs[i][1]]
    else:
        heap[inputs[i][0]].append(inputs[i][1])

for id, scores in heap.items():
    heapq.heapify(scores)
    high_five=heapq.nlargest(5, scores)
    result[id]=sum(high_five)/5
print(result)
