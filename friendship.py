
from printerqueue import Queue


class Node():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<Node: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

    def print_all(self):

        for i in list(self.nodes):
            print(i)


def make_simple_friendship(fr1, fr2, fr3):
    fr1 = Node(fr1)
    fr2 = Node(fr2)
    fr3 = Node(fr3)

    friends = FriendGraph()
    friends.add_people([fr1, fr2, fr3])
    friends.set_friends(fr1, fr2)
    friends.set_friends(fr1, fr3)
    friends.set_friends(fr2, fr3)

    for i in list(friends.nodes):
        print(f'{i.name} is friends with {i.adjacent}')

    return friends


if __name__ == "__main__":
    make_simple_friendship('bob', 'sam', 'tim').print_all()
