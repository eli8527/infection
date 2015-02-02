import uuid
import argparse
import random

__title__ = 'Tester'
__version__ = '1.0'
__author__ = 'Eric Li'

if __name__ == '__main__':
    """
    Generates test csv files for arguments: number of users, number of connections
    and output file destination (csv). Limited to a maximum of 16^6 unique users.
    Number of users must be greater than or equal to two. There are no guarantees
    that all users will be included in the graph.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("num", help="number of users")
    parser.add_argument("edges", help="number of edges")
    parser.add_argument("output", help="output destination")
    args = parser.parse_args()

    # Generate user ids
    users = set()

    for i in range (0,int(args.num)):
        users.add(str(uuid.uuid4().get_hex().upper()[0:6]))

    # writes to output
    file = open(args.output, 'w')

    id1 = users.pop()

    for i in range(0,int(args.edges)):

        # random edge weight b/t 0 and 100
        rand = random.randint(0,100)

        if rand > 60:
            switch = True
        else:
            switch = False

        # clever way to emulate coaches
        if switch:
            users.add(id1)
            id1 = users.pop()

        id2 = users.pop()

        output = '{},{},{}\n'.format(id1,id2,rand)
        file.write(output)


        users.add(id2)

    file.close
