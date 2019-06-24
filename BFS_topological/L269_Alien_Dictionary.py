Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Given the following words in dictionary,

[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]

The correct order is: "wertf".
Example 2:
Given the following words in dictionary,

[
"z",
"x"
]

The correct order is: "zx".
Example 3:
Given the following words in dictionary,

[
"z",
"x",
"z"
]

The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

Solution
Topological sort, time O(mn) m is words count, n is avg word len, space O(1)


###Solution####

import collections

class solution():
    def Order(self,words):
        result, in_degree, out_degree = [], {}, {}
        zero_indegree_queue=collections.deque()
        nodes=set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in range(1,len(words)):
            if (len(words[i-1])>len(words[i]) and words[i-1][:len(words[i])]==words[i]):
                return ""
            self.findEdges(words[i-1],words[i],in_degree,out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_indegree_queue.append(node)

        # BFS starts from here
        while zero_indegree_queue:
            predence=zero_indegree_queue.popleft()
            result.append(predence)

            if predence in out_degree:
                for c in out_degree[predence]:
                    in_degree[c].discard(predence)
                    if not in_degree[c]:
                        zero_indegree_queue.append(c)
                del out_degree[predence]
        if out_degree:
            return ''
        return ''.join(result)

# construct the graph

    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len=min(len(word1),len(word2))
        for i in range(str_len):
            if word1[i]!=word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]]=set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]]=set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break


test=['wrt','wrf','er','ett','rftt']
"""
This is what graph looks like
in_degree= {f:[t],e:[w],t:[r],r:[e]}
out_degree= {t:[f], w:[e],r:[t],e:[r]}
"""
print(solution().Order(test))





