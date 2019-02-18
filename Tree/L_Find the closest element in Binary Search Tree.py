Given a binary search tree and a target node K. The task is to find the node with minimum absolute difference with given target value K.


                                          9
                                       4     17
                                    3    6      22
                                       5   7  20




// For above binary search tree
Input  :  k = 4
Output :  4

Input  :  k = 18
Output :  17

Input  :  k = 12
Output :  9

# Recursive Python program to find key
# closest to k in given Binary Search Tree.

# Utility that allocates a new node with the
# given key and NULL left and right pointers.
class newnode:

    # Constructor to create a new node
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


# Function to find node with minimum
# absolute difference with given K
# min_diff --> minimum difference till now
# min_diff_key --> node having minimum absolute
#                  difference with K

def maxDiffUtil(ptr, k, min_diff, min_diff_key):
    if ptr == None:
        return

    # If k itself is present
    if ptr.key == k:
        min_diff_key[0] = k
        return

    # update min_diff and min_diff_key by
    # checking current node value
    if min_diff > abs(ptr.key - k):
        min_diff = abs(ptr.key - k)
        min_diff_key[0] = ptr.key

        # if k is less than ptr->key then move
    # in left subtree else in right subtree
    if k < ptr.key:
        maxDiffUtil(ptr.left, k, min_diff,
                    min_diff_key)
    else:
        maxDiffUtil(ptr.right, k, min_diff,
                    min_diff_key)

    # Wrapper over maxDiffUtil()


def maxDiff(root, k):
    # Initialize minimum difference
    min_diff, min_diff_key = 999999999999, [-1]

    # Find value of min_diff_key (Closest
    # key in tree with k)
    maxDiffUtil(root, k, min_diff, min_diff_key)

    return min_diff_key[0]


# Driver Code
if __name__ == '__main__':
    root = newnode(9)
    root.left = newnode(4)
    root.right = newnode(17)
    root.left.left = newnode(3)
    root.left.right = newnode(6)
    root.left.right.left = newnode(5)
    root.left.right.right = newnode(7)
    root.right.right = newnode(22)
    root.right.right.left = newnode(20)
    k = 18
    print(maxDiff(root, k))
