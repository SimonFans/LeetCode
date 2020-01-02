Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


"""
1. 将每一个字符串排序后变成list
2. 将每个list变为tuple
3. 建立一个值保存为list的字典，对于每一个相同的tuple，append上对应的字符串
s="bae"
sorted(s) => ['a','b','e'] 
tuple(sorted(s)) => ('a','b','e')
dic[tuple(sorted(s))].append(s)
"""
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=collections.defaultdict(list)
        for s in strs:
            temp_tuple=tuple(sorted(s))
            res[temp_tuple].append(s)
        return res.values()
