class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

    def node_count(self):

        count = 0
        to_visit = [self.root]

        while to_visit:

            current = to_visit.pop()
            if current:
                count += 1

            to_visit.extend(current.children)

        return count


def make_tree(ceo, reports):

    root = Node(ceo, reports)

    tree = Tree(root)

    return tree


if __name__ == '__main__':
    print(make_tree('Jane', ['bob', 'mike',
          'Jes', 'susan']))

    resume = Node("resume.txt", [])
    recipes = Node("recipes.txt", [])
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py", [])
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/", [users])

    tree = Tree(root)
    print(tree.node_count())
