class node:
    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []

    def build_tree(self, node : node):
        if self.root is None: #如果树根为空
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                self.help_queue.pop(0)

    def pre_order(self, current_node:node):
        if current_node:
            print(current_node.elem, end = ' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def mid_order(self, current_node:node):
        if current_node:
            self.mid_order(current_node.lchild)
            print(current_node.elem, end=' ')
            self.mid_order(current_node.rchild)

    def last_order(self, current_node:node):
        if current_node:
            self.last_order(current_node.lchild)
            self.last_order(current_node.rchild)
            print(current_node.elem, end=' ')

    def level_order(self):
        new_queue = []
        new_queue.append(self.root)
        while new_queue:
            out_node = new_queue.pop(0)
            print(out_node.elem, end = ' ')
            if out_node.lchild:
                new_queue.append(out_node.lchild)
            if out_node.rchild:
                new_queue.append(out_node.rchild)


if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(1,11):
        new_node = node(i) #实例化结点
        tree.build_tree(new_node) #把结点放入树中
    tree.pre_order(tree.root) #前序遍历就是深度优先遍历
    print()
    tree.mid_order(tree.root)
    print()
    tree.last_order(tree.root)
    print()
    tree.level_order()