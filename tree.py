(_ROOT, _DEPTH, _BREADTH) = range(3)


class ProgramSegment:
    def __init__(self, identifier, size, parent=None):
        self.identifier = int(identifier)
        self.children = []
        self.parent = parent
        self.size = int(size)
        self.job = None
        self.memory = None

    def add_child(self, identifier):
        self.children.append(identifier)


class Tree:

    def __init__(self):
        self.__nodes = {}
        self.size = 0

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, size, parent=None):
        if parent is None:
            node = ProgramSegment(identifier, size)
        else:
            node = ProgramSegment(identifier, size, self.nodes[parent])
        self[identifier] = node
        self.size += 1
        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=_ROOT):
        children = self[identifier].children
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("\t" * depth, "{0}".format(identifier))
        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call

    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett,
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode == _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode == _BREADTH:
                queue = queue[1:] + expansion  # width-first

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item
