class solution():
    def hasMutualRank(self, user_map, user, rank):
        # 是否被查找的用户在user_map中
        if user not in user_map:
            return False
        # 如果被查找用户list长度小于等于
        if len(user_map[user]) <= rank:
            return False
        # 找到对应用户rank的key
        user_rank_choice = user_map[user][rank]
        if len(user_map[user_rank_choice]) <= rank:
            return False
        # 看当前用户
        return user == user_map[user_rank_choice][rank]

#hasMutualRank('a', 0)
#hasMutualRank('a', 1)
# hasMutualRank('c', 0)

    def changedPairs(self, user_map, user, swap):
        ans = []
        if self.hasMutualRank(user_map, user, swap):
            ans.append(user_map[user][swap])
            return ans
        # make swap
        temp = user_map[user][swap]
        user_map[user][swap] = user_map[user][swap-1]
        user_map[user][swap-1] = temp
        
        if self.hasMutualRank(user_map, user, swap - 1):
            ans.append(user_map[user][swap-1])
            return ans
        # swap back
        temp = user_map[user][swap]
        user_map[user][swap] = user_map[user][swap-1]
        user_map[user][swap-1] = temp
        
        return ans.append(0)   
    
user_map = {'a': ['b', 'c','d'], 'b': ['a', 'd'], 'c': ['a', 'd'], 'd':['a', 'b']}    
s = solution() 
s.hasMutualRank(user_map, 'a', 0)
# s.changedPairs(user_map, 'a', 0)
# s.changedPairs(user_map, 'b', 1)
