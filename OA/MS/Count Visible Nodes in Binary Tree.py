In a binary tree, if in the path from root to the node A, there is no node with greater value than A’s, this node A is visible. 
We need to count the number of visible nodes in a binary tree.

             5
          3     10
       20   21 1
       
return 4.


def count_visible_nodes(root):
	if not root: return 0
	return traverse(root, float('-inf'))

def traverse(node, max_value):
	if not node: return 0
	visible = 1 if node.val >= max_value else 0
	max_value = max(max_value, node.val)
	return traverse(node.left, max_value) + visible + traverse(node.right, max_value)

# RTC: O(N), Space: O(N)
