from user import User

class Graph:
    """
    Represents an undirected graph of users
    """

    # Creates a new graph with no useres
    def __init__(self):
        self.users = {} # Dictionary with key as User, value as adjacent Users

    # Adds a new user with ID id. Returns None if user exists already, else
    # returns the new user.
    def addUser(self, id):
        # If there is already a user of that ID
        if id in self.users:
            return None

        newUser = User(id)

        self.users[id] = newUser
        return newUser


    # Returns a user of ID id if it exists. Returns None otherwise.
    def getUser(self, id):
        if id in self.users:
            return self.users[id]
        else:
            return None

    # Adds an undirected edge between two users with default weight 0
    def addEdge(self, id1, id2, weight = 0):
        if id1 not in self.users:
            self.addUser(id1)
        if id2 not in self.users:
            self.addUser(id2)

        self.users[id1].addNeighbor(self.users[id2], weight)
        self.users[id2].addNeighbor(self.users[id1], weight)

    # Returns all the users in the list
    def getUsers(self):
        return self.users.keys()
