# 讲解：https://www.lintcode.com/problem/86/solution/16938

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._to_next_min(root)

    def hasNext(self):
        return len(self.stack) > 0

    def _next(self):
        if len(self.stack) == 0:
            return None
        next_node = self.stack.pop()
        self._to_next_min(next_node.right)
        return next_node

    def _to_next_min(self, root):
        while root:
            self.stack.append(root)
            root = root.left