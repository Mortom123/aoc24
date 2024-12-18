from dataclasses import dataclass, field
from typing import TypeVar, Generic, List, Callable, Tuple, Self
import heapq

T = TypeVar('T')

@dataclass
class SearchNode(Generic[T]):
    value: T
    cost: float
    heuristic: float = 0
    parents: List[Self] = field(default_factory=list)

    def priority(self):
        return self.cost + self.heuristic
    def __lt__(self, other):
        return self.priority() < other.priority()
    def __gt__(self, other):
        return self.priority() > other.priority()
    def __le__(self, other):
        return self.priority() <= other.priority()
    def __ge__(self, other):
        return self.priority() >= other.priority()


def astar(
        start: T,
        is_goal: Callable[[T], bool],
        get_neighbors: Callable[[T], List[Tuple[T, float]]],
        get_heuristic: Callable[[T], float]
) -> List[SearchNode[T]]:
    q = []
    start_node = SearchNode(value=start, cost=0, heuristic=get_heuristic(start))
    heapq.heappush(q, start_node)

    # Dictionary to store the cost of the cheapest path to a node
    g_costs = {start: 0}
    nodes = {start: start_node}

    goal_paths = []
    while q:
        current_node: SearchNode[T] = heapq.heappop(q)
        current_cost = current_node.cost

        if is_goal(current_node.value):
            goal_paths.append(current_node)

        if len(goal_paths) and current_cost > goal_paths[0].cost:
            break

        for neighbor, n_cost in get_neighbors(current_node.value):
            n_cost = current_cost + n_cost

            if neighbor not in g_costs or n_cost < g_costs[neighbor]:
                g_costs[neighbor] = n_cost
                h_cost = get_heuristic(neighbor)
                neighbor_node = SearchNode(value=neighbor, parents=[current_node], cost=n_cost, heuristic=h_cost)
                nodes[neighbor] = neighbor_node
                heapq.heappush(q, neighbor_node)
                continue

            if n_cost == g_costs[neighbor]:
                nodes[neighbor].parents.append(current_node)

    return goal_paths

def get_path(node: SearchNode[T]) -> List[T]:
    if not len(node.parents):
        return [node.value]
    parent = node.parents[0]
    return get_path(parent) + [node.value]

def get_paths(node: SearchNode[T]) -> List[List[T]]:
    if not len(node.parents):
        return [[node.value]]

    paths = []
    for p in node.parents:
        parent_paths = get_paths(p)
        for pp in parent_paths:
            paths.append(pp + [node.value])
    return paths

if __name__ == "__main__":
    #  A
    # / \
    # B C
    # \ /
    #  D

    def get_neighbors(node: str) -> List[Tuple[str, float]]:
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('D', 4)],
            'C': [('A', 4), ('D', 1)],
            'D': [('B', 4), ('C', 1)]
        }
        return graph.get(node, [])

    def get_heuristic(node: str) -> float:
        heuristic = {
            'A': 5,
            'B': 4,
            'C': 1,
            'D': 0
        }
        return heuristic.get(node, float('inf'))

    start = 'A'
    goal = 'D'
    ns = astar(start, lambda x: x==goal, get_neighbors, get_heuristic)
    for n in ns:
        print("Path:", n.cost, get_paths(n), get_path(n))
