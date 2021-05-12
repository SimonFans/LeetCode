题目有点长，链接在此：https://leetcode.com/problems/snakes-and-ladders/
  
Solution:
  
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def label_to_position(label, n):
            r, c = divmod(label-1, n)
            # row = 偶数, 即从左往右递增
            if r % 2 == 0:
                return n-1-r, c
            # row = 奇数, 即从左往右递减
            else:
                return n-1-r, n-1-c
            
        rows = len(board)
        #左上角的label为最终目的地
        target_label  = rows * rows
        # dist会记录label：steps
        dist = {1: 0}
        # BFS, 初始放置左下角label
        queue = collections.deque([1])
        while queue:
            current_label = queue.popleft()
            # 如果正好走到目的地的label，则返回对应的step数目
            if current_label == target_label:
                return dist[current_label]
            for next_label in range(current_label + 1, min(current_label + 6, target_label) + 1):
                r, c = label_to_position(next_label, rows)
                if board[r][c] != -1:
                    next_label = board[r][c]
                if next_label not in dist:
                    dist[next_label] = dist[current_label] + 1
                    queue.append(next_label)
        return -1
      
