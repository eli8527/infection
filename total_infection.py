from user import User
from graph import Graph
from Queue import Queue

def total_infection(graph, initial):
    """
    Performs a total infection of an entire connected component of a given graph
    from an initial starting point using BFS. Returns a list of infected users
    and returns None if the initial point does not exist.
    """

    if initial not in graph.getUsers():
        return None

    queue = Queue()
    initialUser = graph.getUser(initial)

    # Inserts initial user into queue
    queue.put(initialUser)
    infected = set()

    # BFS
    while not queue.empty():
        user = queue.get()

        if user not in infected:
            user.version = 'new'
            infected.add(user)

            for neighbor in user.getNeighbors():
                queue.put(neighbor)

    return infected
