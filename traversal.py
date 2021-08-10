class Tree(object):
    def __init__(self, val=1):
        self.left = None
        self.right = None
        self.val = val
        return

    def make_left(self, val: int):
        self.left = Tree(val)
        return self.left

    def make_right(self, val):
        self.right = Tree(val)
        return self.right


tt = Tree()
tt.make_left(2).make_left(3).make_right(4).make_right(5)
tt.left.left.make_left(6)
tt.make_right(7).make_left(8).make_right(9)


def dfs(tree: Tree) -> None:
    # traverse and print all elements
    to_traverse = [tree]
    while to_traverse:
        node = to_traverse.pop(-1)
        if node.right is not None:
            to_traverse.append(node.right)
        if node.left is not None:
            to_traverse.append(node.left)
        print("Now at Node({})".format(node.val))
    return


def dfs_rec(tree: Tree):
    # base case
    print("Now at Node({})".format(tree.val))
    if tree.left is None and tree.right is None:
        return
    if tree.left is not None:
        dfs_rec(tree.left)
    if tree.right is not None:
        dfs_rec(tree.right)
    return


def bfs(tree: Tree):
    to_traverse = [tree]
    while to_traverse:
        node = to_traverse.pop(0)
        if node.left is not None:
            to_traverse.append(node.left)
        if node.right is not None:
            to_traverse.append(node.right)
        print("Now at Node({})".format(node.val))
    return


if __name__ == "__main__":
    print("-"*80)
    print("DFS")
    dfs(tt)

    print("^"*80)
    print("DFS(Recursive)")
    dfs_rec(tt)

    print("-"*80)
    print("BFS")
    bfs(tt)
