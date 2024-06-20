class TreeNode:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.data = key


class BinaryTree:
    def _init_(self, root):
        self.root = TreeNode(root)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    
    def top_view(self):
        if not self.root:
            return
        queue = [(self.root, 0)]
        hd_map = {}
        while queue:
            node, hd = queue.pop(0)
            if hd not in hd_map:
                hd_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        for key in sorted(hd_map.keys()):
            print(hd_map[key], end=' ')

    
    def left_view(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    print(node.data, end=' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

if __name__ == '_main_':
    
    bt = BinaryTree(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)
    bt.root.right.left = TreeNode(6)
    bt.root.right.right = TreeNode(7)

    print("Preorder traversal:")
    bt.preorder(bt.root)
    print("\nPostorder traversal:")
    bt.postorder(bt.root)
    print("\nTop view:")
    bt.top_view()
    print("\nLeft view:")
    bt.left_view()