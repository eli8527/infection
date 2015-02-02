class User:
    """
    Represents a user instance in a coaching network graph. Attributes include
    user id and site version used.
    """

    # Creates a new user with ID id
    def __init__(self, id):
        self.id = id # User's ID
        self.version = 'old' # Version - assume there are only two: old and new
        self.neighbors = {}

    # String representation of the user
    def __str__(self):
        return 'ID: ' + str(self.id) + ', Version: ' + str(self.version)

    # Adds a neighbor to the user
    def addNeighbor(self, nbr, weight):
        self.neighbors[nbr] = weight

    # Returns all the adjacent users to the current user
    def getNeighbors(self):
        return self.neighbors.keys()

    # Returns the weight of the edge connectiong the user to another adj. user
    def getWeight(self, nbr):
        return self.neighbors[nbr]

    # Returns the degree of the user (how many connections it has)
    def getDegree(self):
        return len(self.neighbors.keys())
