from dataclasses import dataclass, field
from typing import Optional, TypeVar, Generic, List, Callable, Tuple, Self
import heapq

T = TypeVar('T')

@dataclass
class CompareNode(Generic[T]):
    value: T = field(compare=False)
    parent: Optional[Self] = field(compare=False, default=None)
    cost: float = field(compare=False, default=0)
    heuristic: float = field(compare=False, default=0)

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
) -> Optional[CompareNode[T]]:
    q = []
    start_node = CompareNode(value=start, cost=0, heuristic=get_heuristic(start))
    heapq.heappush(q, start_node)

    # Dictionary to store the cost of the cheapest path to a node
    g_costs = {start: 0}

    while q:
        current_node = heapq.heappop(q)

        if is_goal(current_node.value):
            return current_node

        current_cost = g_costs[current_node.value]
        for neighbor, n_cost in get_neighbors(current_node.value):
            n_cost = current_cost + n_cost

            if neighbor not in g_costs or n_cost < g_costs[neighbor]:
                g_costs[neighbor] = n_cost
                h_cost = get_heuristic(neighbor)
                neighbor_node = CompareNode(value=neighbor, parent=current_node, cost=n_cost, heuristic=h_cost)
                heapq.heappush(q, neighbor_node)
    return None

@dataclass
class MultiCompareNode(Generic[T]):
    value: T = field(compare=False)
    parents: List[Self] = field(compare=False, default_factory=list)
    cost: float = field(compare=False, default=0)
    heuristic: float = field(compare=False, default=0)

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


def astar_multipath(
        start: T,
        is_goal: Callable[[T], bool],
        get_neighbors: Callable[[T], List[Tuple[T, float]]],
        get_heuristic: Callable[[T], float]
) -> List[MultiCompareNode[T]]:
    q = []
    start_node = MultiCompareNode(value=start, cost=0, heuristic=get_heuristic(start))
    heapq.heappush(q, start_node)

    # Dictionary to store the cost of the cheapest path to a node
    g_costs = {start: 0}
    nodes = {start: start_node}

    goal_paths = []
    while q:
        current_node = heapq.heappop(q)

        if is_goal(current_node.value):
            goal_paths.append(current_node)

        current_cost = g_costs[current_node.value]

        if len(goal_paths) and current_cost > goal_paths[0].cost:
            break

        for neighbor, n_cost in get_neighbors(current_node.value):
            n_cost = current_cost + n_cost

            if neighbor not in g_costs or n_cost < g_costs[neighbor]:
                g_costs[neighbor] = n_cost
                h_cost = get_heuristic(neighbor)
                neighbor_node = MultiCompareNode(value=neighbor, parents=[current_node], cost=n_cost, heuristic=h_cost)
                nodes[neighbor] = neighbor_node
                heapq.heappush(q, neighbor_node)
                continue

            if n_cost == g_costs[neighbor]:
                nodes[neighbor].parents.append(current_node)

    return goal_paths


def get_path(node: CompareNode[T]) -> List[T]:
    path = []
    while node:
        path.append(node.value)
        node = node.parent
    path.reverse()
    return path

if __name__ == "__main__":
    def get_neighbors(node: str) -> List[Tuple[str, float]]:
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)]
        }
        return graph.get(node, [])

    def get_heuristic(node: str) -> float:
        heuristic = {
            'A': 5,
            'B': 3,
            'C': 1,
            'D': 0
        }
        return heuristic.get(node, float('inf'))

    start = 'A'
    goal = 'D'
    n = astar(start, lambda x: x==goal, get_neighbors, get_heuristic)
    print("Path:", n.cost, get_path(n))
