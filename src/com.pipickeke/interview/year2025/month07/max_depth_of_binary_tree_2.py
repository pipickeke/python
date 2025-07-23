
"""
二叉树的最大深度（Maximum Depth of Binary Tree）

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(f"结果：{max_depth(root)}")


