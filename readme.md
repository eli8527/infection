Khan Academy Limited Infection
====

This project includes implementations of several infection schemes described by Khan Academy in their limited infection interview specification as well as a visualization of the final infected graph. Included is `tester.py` that allows the user to automate testing of the infection algorithms.

## Requirements
Be sure that the following are installed:

- Python (at least 2.7)
- `networkx` and `matplotlib`, both of which can be installed using `pip`. To install, type `pip install networkx matplotlib`.

## Instructions

There are several options for running this python script. Each option requires a csv data file with each line formatted `user1, user2, weight`. This means that `user1` is connected to `user2` on an edge with weight `weight`. Several examples are included in the `input/` folder. After running each version, follow the onscreen prompts to perform one of the three types of infections. 

To run the basic version, type:

```python
python infection.py data.csv
```

To run a version with infection visualization, type:

```python
python infection.py -v data.csv
```
The infection visualization version creates a graph at the end of running that shows all the users and which users are infected. It then produces a `png` file of that image that is saved in the data file's directory titled `data_infected.png`. One can run `python infection.py -h` if they need help.

One can also run `tester.py` to generate more randomized test cases. In general, `tester.py` can be run as follows:

```python
python tester.py 10 100 random.csv
```
This produces a random edge data file with no more than 10 users and 100 edges. One can change the parameters as they see fit. For more information, type `python tester.py -h`. Heuristically, this program generates a given number of UUIDs and then creates a random graph based csv file. To simulate coach-student relationships better, I implement a switch that randomly flops the coach with `p = .4`.

## Infection Heuristics
In here are three infection heuristics that are implemented as per the specifications outlined by Khan Academy. In all cases, the user network is represented as a graph using adjacency lists.

### Total Infection
Total infection uses breadth-first search (BFS) to infect all users of the initial user's connected component. This is a relatively straightforward algorithm.

### Limited Infection
This is an extension on total infection in that we only want a limited number of users to be infected. To accomplish this, we still use BFS. However, there are several changes to our heuristic.

First, we don't necessarily start from the initial user provided. Based on the initial user, we find the neighbor that has the highest degree. Intuitively, it makes sense to start from the neighbor of heighest degree because in a real network, the coaches will usually be the most connected. We are, of course, assuming that the student and coach are directly connected, which is not too outrageous of an assumption. By picking the initial infection point to be the user of highest degree closest to the given user, we are almost always going to guarantee that the coach will be infected (in a typical classroom setting). The next step is to determine which students to infect.

To do this, we implement a thresholding heuristic. Specifically, we examine the edge weights between the initial user and its neighbors. We ask the user to input a specific threshold. If there was more time, I could probably find a way to have the algorithm automatically detect the optimal threshold. For now, let us specify some examples of edge weight schemes that are sensible.

- **Time spent together:** Each edge weight represents the cumulative number of time both the coach and student were present on the Khan Academy website. By setting a specific threshold, it would be possible to only infect those that were very active, somewhat active, or minimally active.
- **Ranking:** Each edge weight represents a student's ranking relative to the coach. This ranking could be determined by the coach or by the student's abilities to do problems without help. One possible benefit of this, combined with thresholding, is the following. Perhaps there is a new update to the site that greatly enhances self learning and creating exercises. It is sensible that we might want those that are struggling to comprehend the material to receive access to this site first.

### Exact Infection
This is a very slight modification of **limited infection** where we only infect if we can find an infection scheme that fits both the given number of clients to infect as well as the threshold. Otherwise, no infection occurs

## Extensions
One idea that I would like to explore is implementing an exact infection using `A*` or a better heuristic. Another approach could be specifying a set number and threshold, but not specifying the initial user. The program would then systematically search through every "class" until it finds one that satisfies the conditions **and** infects the entire connected component.

It would also be interesting to explore a more interactive data visualization rather than just producing the plot at the end. There are several good Python libraries for this, and it would also be worth exploring more famous Javascript libraries such as `D3.js`.

## Contact
For questions, comments, suggestions, or errata, feel free to reach out to me at:
> Eric Li
> eyli@princeton.edu