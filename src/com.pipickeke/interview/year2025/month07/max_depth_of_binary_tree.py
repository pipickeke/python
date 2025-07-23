"""

 二叉树的最大深度（Maximum Depth of Binary Tree）
"""

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))



# 测试用例
def test_max_depth():
    #1,空树
    assert max_depth(None) == 0, 'Test case 1 failed: empty tree'

    #2,单节点树
    root1 = TreeNode(1)
    assert max_depth(root1) == 1, 'Test case 2 failed: single node tree'

    #3,只有左子树的树
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    assert max_depth(root2) == 3, 'Test case 2 failed: single node tree'

    #4,完全二叉树
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)





if __name__ == '__main__':
    test_max_depth()











