test_str = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open('2022/puzzle_inputs/7.txt', 'r') as file:
    strInput = file.read()

from collections import deque

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', size=0, children=None, parent=None):
        self.name = name
        self.size = size
        self.size_plus_children = 0
        self.parent = parent
        self.children = children
        if children:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        if self.children is not None:
            self.children.append(node)
        else:
            self.children = [node]
    def get_all_size(self):
        if self.children is None:
            return self.size
        else:
            for child in self.children:
                print("child.get_all_size()", child.name, child.size)
                return self.size + child.get_all_size()

def DFS(node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    # this almost works but i'm going in the reverse order
    # need to grab the final child first then fill out 
    while stack:
        s = stack.pop()
        print(s, end = " ")
        s.size_plus_children  = s.size

        if s.children:
            for n in s.children:
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
                    s.size_plus_children += n.size_plus_children
    return True

def updateNodeSize(node):
    """Post order tree traversal"""
    if not node.children:
        if node.size:
            node.size_plus_children = node.size
            return node.size
        return 0

    cumulative_size = node.size
    for child in node.children:
        cumulative_size += updateNodeSize(child)
    node.size_plus_children += cumulative_size
    return cumulative_size


root = Tree('\\')
current_node = root
file_system = strInput.split('\n')
# rolling_sum = 0
for event in file_system[1:-1]:
    if event == '$ cd ..':
        # current_node.size += rolling_sum
        # rolling_sum = 0
        current_node = current_node.parent
    elif '$ cd ' in event:
        # current_node.size += rolling_sum
        for child in current_node.children:
            if child.name == event.split(' ')[2]:
                current_node = child
        # print(current_node)
        # rolling_sum = 0
    elif 'dir' in event:
        current_node.add_child(Tree(name=event.split(' ')[1],parent=current_node))
        # print(current_node.children)
        continue
    elif '$ ls' in event:
        continue
    else:
        current_node.size += int(event.split(' ')[0])

# print(root.get_all_size())
# print(DFS(root))
updateNodeSize(root)
print(root.size_plus_children, root.size) # this has d and e but not a...
print(root.children[0].size_plus_children, root.children[0].size)
print(root.children[1].size_plus_children, root.children[1].size)

# now that i have the right values
# recursively traverse the tree, order doesn't matter and add up directories where size
threshold = 100_000

def DFS_sum(node, threshold):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    sum = 0
    # this almost works but i'm going in the reverse order
    # need to grab the final child first then fill out 
    while stack:
        s = stack.pop()
        # print(s, s.size_plus_children)
        if(s.size_plus_children < threshold):
            sum += s.size_plus_children

        if s.children:
            for n in s.children:
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
    return sum

# 1 - 1543140
print('solution1',DFS_sum(root, threshold)) # 1543140

# part 2 solution
# choose a file to delete
used_space = root.size_plus_children
disk_space = 70_000_000
unused_space_reqd = 30_000_000
dir_size = unused_space_reqd - (disk_space - used_space)
# find the directory whose size is closest to but greater than dir_size


def DFS_nearest(node, threshold):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    actual_dir_size = 70_000_000
    # this almost works but i'm going in the reverse order
    # need to grab the final child first then fill out 
    while stack:
        s = stack.pop()
        # print(s, s.size_plus_children)
        if(s.size_plus_children > threshold):
            actual_dir_size = min(actual_dir_size, s.size_plus_children)

        if s.children:
            for n in s.children:
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
    return actual_dir_size

# 2 - 1117448
print(DFS_nearest(root, dir_size))
