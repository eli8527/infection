from user import User
from graph import Graph
from Queue import Queue

def limited_infection(graph, initial, num, threshold):
    """
    Infects approximately num of users given an initial user. This is a
    relatively naive algorithm that first finds the "parent" and then infects
    those that are a certain edge weighted threshold. This scheme allows for
    the teacher to be more or less always infected, and to perform an infection
    from that initial point of all the children that are of a certain edge
    threshold.

    Returns a list of total infected, and None if invalid parameters
    """
    if initial not in graph.getUsers():
        return None

    if not num:
        return None

    queue = Queue()
    initialUser = graph.getUser(initial)

    # Lets start from the user of highest degree that is directly reachable from
    # the initial user. In most cases, this will likely be a teacher. We can
    # safely make this assumption because in the typical use case, a student
    # is directly connnected with his or her teacher
    maxDegree = initialUser.getDegree()
    maxUser = initialUser

    for neighbor in initialUser.getNeighbors():
        if neighbor.getDegree() > maxDegree:
            maxUser = neighbor
            maxDegree = neighbor.getDegree()

    # Inserts max user into queue
    queue.put(maxUser)
    infected = set()

    # BFS with Thresholding
    while not queue.empty():
        user = queue.get()

        if user not in infected:

            # Only infects user if the number of infected is lesser than the
            # number specified. This has obvious trade offs. But combined with
            # thresholding, should give a better result than if thresholding
            # was not included
            if len(infected) < num:
                user.version = 'new'
                infected.add(user)
            else:
                return infected

            for neighbor in user.getNeighbors():

                # add to queue only if the edge weight b/t the two is greater
                # than the given threshold
                if user.getWeight(neighbor) >= threshold:
                    queue.put(neighbor)

    return infected
